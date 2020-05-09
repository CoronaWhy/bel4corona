# -*- coding: utf-8 -*-

"""Tools for acquiring and normalizing the content from BioDati's demo server."""

import json
import os

import click

import pybel.grounding

HERE = os.path.abspath(os.path.dirname(__file__))
NETWORK_ID = '01E46GDFQAGK5W8EFS9S9WMH12'
RAW_PATH = os.path.join(HERE, 'covid19-biodati-raw.bel.nodelink.json')
GROUNDED_PATH = os.path.join(HERE, 'covid19-biodati-grounded.bel.nodelink.json')


@click.command()
@click.option('--force', is_flag=True)
@click.option('--user', prompt=True)
@click.password_option()
def main(force: bool, user: str, password: str):
    """Download and dump the BioDati 'rona graph."""
    if not os.path.exists(GROUNDED_PATH) and not force:
        if not os.path.exists(RAW_PATH) and not force:
            graph = pybel.from_biodati(
                network_id=NETWORK_ID,
                username='demo@biodati.com',
                password='demo',
                base_url='https://networkstore.demo.biodati.com',
            )
            pybel.dump(graph, RAW_PATH)

        graph = pybel.load(RAW_PATH)

        # This will probably not work for you (yet!)
        graph = pybel.grounding.ground(graph)
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
