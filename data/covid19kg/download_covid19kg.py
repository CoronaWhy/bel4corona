# -*- coding: utf-8 -*-

"""Tools for acquiring and normalizing the content from Fraunhofer."""

import click
import json
import os
from urllib.request import urlretrieve

import pybel

HERE = os.path.abspath(os.path.dirname(__file__))
COMMIT = 'd3c57d0e324886288d5e25c7388bcfdba62f31dd'
URL = f'https://github.com/covid19kg/covid19kg/raw/{COMMIT}/covid19kg/_cache.bel.nodelink.json'
RAW_PATH = os.path.join(HERE, 'covid19-fraunhofer-raw.bel.nodelink.json')
GROUNDED_PATH = os.path.join(HERE, 'covid19-fraunhofer-grounded.bel.nodelink.json')


@click.command()
@click.option('--force', is_flag=True)
@click.option('--user', prompt=True)
@click.password_option()
def main(force: bool, user: str, password: str):
    """Download and dump the Fraunhofer 'rona graph."""
    if not os.path.exists(GROUNDED_PATH) and not force:
        if not os.path.exists(RAW_PATH) and not force:
            urlretrieve(URL, RAW_PATH)
        graph = pybel.load(RAW_PATH)
        graph.version = COMMIT

        # This will probably not work for you (yet!)
        graph = graph.ground()
        graph.summarize()

        pybel.dump(graph, GROUNDED_PATH)
    else:
        graph = pybel.load(GROUNDED_PATH)

    res = pybel.to_bel_commons(
        graph=graph,
        host='https://bel.labs.coronawhy.org',
        user=user,
        password=password,
    )
    click.secho(json.dumps(res.json(), indent=2))


if __name__ == '__main__':
    main()
