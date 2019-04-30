import uuid

import click


@click.group()
def uid():
    """Time tool."""
    pass


@uuid.command()
def u4():
    print(str(uuid.uuid4()))
