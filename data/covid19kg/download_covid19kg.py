# -*- coding: utf-8 -*-

"""Tools for acquiring and normalizing the content from Fraunhofer."""

import click
import os
from urllib.request import urlretrieve

import pybel.grounding

HERE = os.path.abspath(os.path.dirname(__file__))
URL = 'https://raw.githubusercontent.com/covid19kg/covid19kg/master/covid19kg/_cache.bel.nodelink.json'
RAW_PATH = os.path.join(HERE, 'covid19kg-raw.bel.nodelink.json')
GROUNDED_PATH = os.path.join(HERE, 'covid19kg-grounded.bel.nodelink.json')


@click.command()
def main():
    """Download and dump the Fraunhofer 'rona graph."""
    if not os.path.exists(RAW_PATH):
        urlretrieve(URL, RAW_PATH)

    graph = pybel.load(RAW_PATH)

    # This will probably not work for you (yet!)
    graph = pybel.grounding.ground(graph)
    graph.summarize()

    pybel.dump(graph, GROUNDED_PATH)


if __name__ == '__main__':
    main()
