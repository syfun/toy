# coding=utf-8

from __future__ import print_function

import hashlib
import base64
import os

import click


@click.command()
@click.option('-f', default=False, help='Follow a file.')
@click.option('-b', default=False, help='Print base64 string or not.')
@click.argument('value')
def cli(f, b, value):
    if not f:
        s = hashlib.md5(value).hexdigest()
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
        print(base64.b64encode(s))
    else:
        print(s)


if __name__ == '__main__':
    cli()
