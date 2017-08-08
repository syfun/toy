import hashlib
import base64
import os

import click


@click.command()
@click.option('-f', is_flag=True, help='Follow a file or not.')
@click.option('-b', is_flag=True, help='Print base64 string or not.')
@click.argument('value')
def md5(f, b, value):
    """Get md5."""
    if not f:
        s = hashlib.md5(value.encode()).hexdigest()
    else:
        if not os.path.exists(value):
            raise Exception('{} not existed.'.format(value))
        if not os.path.isfile(value):
            raise Exception('{} is not a file.'.format(value))
        m = hashlib.md5()
        with open(value, 'rb') as f:
            while 1:
                buffer = f.read(4096)
                if not buffer:
                    break
                m.update(buffer)
        s = m.hexdigest()
    if b:
        click.echo(base64.b64encode(s.encode()))
    else:
        click.echo(s)
