# -*- coding: utf-8 -*-

"""Tools for acquiring and normalizing the content from INDRA."""

import click
import os

import pybel

HERE = os.path.abspath(os.path.dirname(__file__))
PATH = os.path.join(HERE, 'covid19-indra.bel.nodelink.json')


@click.command()
def main():
    """Download and dump the INDRA 'rona graph."""
    graph = pybel.from_emmaa('covid19')
    pybel.dump(graph, 'covid19-indra.bel.nodelink.json')


if __name__ == '__main__':
    main()
