import uuid

import click


@click.group()
def uid():
    """UUID tool."""
    pass


@uid.command()
def u4():
    print(str(uuid.uuid4()))
