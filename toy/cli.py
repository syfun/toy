import click

from .b64 import b64
from .get24 import get24
from .md5 import md5
from .tt import tt
from .t import t


@click.group()
def main():
    pass


main.add_command(tt)
main.add_command(md5)
main.add_command(get24)
main.add_command(b64)
main.add_command(t)
