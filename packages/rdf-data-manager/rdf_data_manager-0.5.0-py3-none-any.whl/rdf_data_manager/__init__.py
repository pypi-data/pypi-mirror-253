import logging
import sys
import time
import traceback
from dataclasses import dataclass

import boto3
import requests

from argparse import ArgumentParser
from pathlib import Path

from requests.auth import HTTPDigestAuth
from tqdm import tqdm

from rdflib import Dataset, Graph
from rdflib.exceptions import ParserError

# tqdm opt
TQDM_OPTS = {
    "ncols": 100,
    "ascii": True,
    "desc": "Uploading",
}


UPLOAD_GRAPH_CHUNK_SIZE = 10000


@dataclass
class VirtuosoCredentials:
    url: str
    user: str
    password: str


def redo_if_failure(call, max_redo=3, sleep_time=5, *args, **kwargs):
    """Redo a function if it fail, with a sleep time between each try"""
    i = 0
    while True:
        i += 1
        try:
            return call(*args, **kwargs)
        except Exception as e:
            if i == max_redo:
                raise (e)
            traceback.print_exc(file=sys.stdout)
            logging.debug(
                "Fail to execute {}. Retrying in {} sec...".format(
                    call.__name__, sleep_time
                )
            )
            time.sleep(sleep_time)
            sleep_time = sleep_time * 2
            continue  # redo


def delete_graph(virtuoso_credentials, graph_uri):
    logging.info(f"Deleting graph {graph_uri}")
    response = requests.delete(
        f"{virtuoso_credentials.url}/sparql-graph-crud-auth?",
        auth=HTTPDigestAuth(virtuoso_credentials.user, virtuoso_credentials.password),
        params={"graph-uri": graph_uri},
    )
    if response.status_code == 404:
        logging.info(f"Graph {graph_uri} doesn't exist")
    else:
        response.raise_for_status()
        # give virtuoso enough time to delete the graph
        time.sleep(3)


def _upload_graph(virtuoso_credentials, graph_uri, graph):
    response = redo_if_failure(
        requests.post,
        3,
        5,
        f"{virtuoso_credentials.url}/sparql-graph-crud-auth",
        auth=HTTPDigestAuth(virtuoso_credentials.user, virtuoso_credentials.password),
        params={"graph-uri": graph_uri},
        data=graph.serialize(format="ttl", encoding="utf-8"),
        headers={"Content-type": "text/plain"},
    )
    response.raise_for_status()


def upload_graph(
    virtuoso_credentials,
    graph_uri,
    graph,
    filename,
):
    g = Graph()
    nb_loops_total = len(g) // UPLOAD_GRAPH_CHUNK_SIZE + 1
    nb_loops_current = 0

    for triple in graph:
        g.add(triple)
        len_g = len(g)
        if len_g >= UPLOAD_GRAPH_CHUNK_SIZE:
            nb_loops_current += 1
            logging.info(
                f"Uploading {len_g} triples from {filename} into graph {graph_uri} ({nb_loops_current} / {nb_loops_total})"
            )
            _upload_graph(virtuoso_credentials, graph_uri, g)
            g = Graph()
    _upload_graph(virtuoso_credentials, graph_uri, g)


def main():
    parser = ArgumentParser()
    parser.add_argument("--input-type", choices=["s3", "fs"], required=True)

    parser.add_argument("--s3-url", type=str)
    parser.add_argument("--s3-access-key", type=str)
    parser.add_argument("--s3-secret-key", type=str)
    parser.add_argument("--s3-bucket", type=str)
    parser.add_argument("--s3-dirs", type=str, nargs="+")

    parser.add_argument("--input-dirs", type=Path, nargs="+")

    parser.add_argument("--virtuoso-url", type=str, required=True)
    parser.add_argument("--virtuoso-user", type=str, required=False, default="dba")
    parser.add_argument("--virtuoso-password", type=str, required=False, default="dba")

    parser.add_argument("--rdf-graph", type=str, required=True)
    parser.add_argument("--delete-graph", action="store_true")
    parser.add_argument("--delete-only", action="store_true")

    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-p", "--progress", action="store_true", default=False)

    args = parser.parse_args()

    # Set verbosity
    VERBOSITY_MAPPING = {0: logging.WARNING, 1: logging.INFO, 2: logging.DEBUG}
    verbosity = args.verbose if args.verbose < 3 else 2
    logging.basicConfig(level=VERBOSITY_MAPPING[verbosity])

    virtuoso_credentials = VirtuosoCredentials(
        args.virtuoso_url,
        args.virtuoso_user,
        args.virtuoso_password,
    )

    # Delete graph before upload
    if args.delete_graph or args.delete_only:
        delete_graph(
            virtuoso_credentials,
            args.rdf_graph,
        )

    if args.input_type == "s3":
        s3_resource = boto3.resource(
            "s3",
            endpoint_url=args.s3_url,
            aws_access_key_id=args.s3_access_key,
            aws_secret_access_key=args.s3_secret_key,
        )

        # upload all files to graph
        if not args.delete_only:
            s3_bucket = s3_resource.Bucket(args.s3_bucket)

            # if no s3_dirs specified, we will loop on all files in the bucket
            prefixes = args.s3_dirs if args.s3_dirs else [""]

            for prefix in prefixes:
                # count object first
                total = sum(1 for _ in s3_bucket.objects.filter(Prefix=prefix))
                logging.info(
                    f"Upload {total} files form {args.s3_bucket}/{prefix} into"
                    f" {args.rdf_graph}"
                )
                # iter to upload
                for obj in tqdm(
                    s3_bucket.objects.filter(Prefix=prefix),
                    total=total,
                    disable=(not args.progress),
                    **TQDM_OPTS,
                ):
                    rdf_string = obj.get()["Body"].read().decode("utf-8")

                    response = redo_if_failure(
                        requests.post,
                        3,
                        5,
                        f"{virtuoso_credentials.url}/sparql-graph-crud-auth",
                        auth=HTTPDigestAuth(
                            virtuoso_credentials.user,
                            virtuoso_credentials.password,
                        ),
                        params={"graph-uri": args.rdf_graph},
                        data=rdf_string.encode("utf-8"),
                        headers={"Content-type": "text/plain"},
                    )
                    response.raise_for_status()
    else:
        for input_dir in args.input_dirs:
            total = sum(1 for filepath in input_dir.rglob("*") if not filepath.is_dir())
            logging.info(f"Found {total} files in {input_dir}")
            for filepath in tqdm(
                input_dir.rglob("*"),
                total=total,
                disable=(not args.progress),
                **TQDM_OPTS,
            ):
                if not filepath.is_dir():
                    logging.info(f"Processing file {filepath}")
                    try:
                        if filepath.suffix in [".nquads", ".trig"]:
                            dataset = Dataset()
                            dataset.parse(filepath)
                            for g in dataset.graphs():
                                if len(g) == 0:
                                    logging.info(f"Skipping empty graph {g.identifier}")
                                    continue
                                delete_graph(
                                    virtuoso_credentials,
                                    g.identifier,
                                )
                                upload_graph(
                                    virtuoso_credentials,
                                    g.identifier,
                                    g,
                                    filepath.name,
                                )
                        else:
                            g = Graph()
                            g.parse(filepath)
                            if len(g) == 0:
                                logging.info(f"Skipping empty file {filepath}")
                                continue
                            upload_graph(
                                virtuoso_credentials,
                                args.rdf_graph,
                                g,
                                filepath.name,
                            )
                    except ParserError:
                        logging.error(
                            f"Skipping file {filepath} because of parse error."
                        )


if __name__ == "__main__":
    main()
