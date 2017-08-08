import base64

import click


@click.group()
def b64():
    """Base64 encode or decode."""
    pass


@b64.command()
@click.argument('string')
def encode(string):
    """Encode"""
    click.echo(base64.b64encode(string.encode()))


@b64.command()
@click.argument('string')
def decode(string):
    """Decode"""
    click.echo(base64.b64decode(string.encode()))
