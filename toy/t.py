import arrow

import click

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


@click.group()
def t():
    """Time tool."""
    pass


@t.command()
def now():
    """Time Now"""
    n = arrow.now()
    print("Time Now: \n")
    print(n)
    print("Unix timestamp: ", n.float_timestamp)
