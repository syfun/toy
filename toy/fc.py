"""
Example:
    python fc.py find ./src --skipexts="jpg,jpeg,png,ico,svg" --onlyexts="html"
    python fc.py find ./login.html --one true
 
    python fc.py replace ./src --skipexts="jpg,jpeg,png,ico,svg" --onlyexts="html" --file out.json
    python fc.py replace ./login.html --one true --file out.json
"""

from __future__ import print_function

import codecs
import json
import os
import re

import click
from scandir import scandir

P = re.compile(u'[\u4e00-\u9fff]+')
CHINESE = {}


def read(filename, kv=None):
    print(filename)
    chinese = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            # print line
            m = P.findall(line.decode('utf-8'))
            if m:
                for i in m:
                    chinese[i] = ""
    if not kv:
        CHINESE.update(chinese)
    else:
        with open(filename, 'r') as f:
            b = f.read()
        with open(filename, 'w') as f:
            for c in chinese:
                v = kv.get(c)
                if v:
                    b = b.replace(c.encode('utf-8'), v.encode('utf-8'))
            f.write(b)


def handle_dir(dirname, skip, skipexts, onlyexts, kv=None):
    if not os.path.isdir(dirname):
        raise Exception('{} not a directory.'.format(dirname))
    for entry in scandir(dirname):
        if entry.name in skip:
            continue
        if entry.is_file():
            ext = entry.name.split('.')[-1]
            if onlyexts and ext not in onlyexts:
                continue
            if skipexts and ext in skipexts:
                continue
            read(entry.path, kv=kv)
        elif entry.is_dir():
            handle_dir(entry.path, skip, skipexts, onlyexts, kv=kv)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('src')
@click.option('--skip', default='',
              help='skip dir or file, please split with ",".', type=str)
@click.option('--skipexts', default='',
              help='skip extensions,  please split with ",".', type=str)
@click.option('--onlyexts', default='',
              help='only extensions, please split with ",".', type=str)
@click.option('--one', default=False,
              help='one file, not dir.', type=bool)
def find(src, skip, skipexts, onlyexts, one):
    if one:
        if not os.path.isfile(src):
            raise Exception('{} not a file.'.format(src))
        read(src)
    else:
        handle_dir(src, skip, skipexts, onlyexts)
    with codecs.open('out.json', 'w', 'utf-8') as f:
        f.write(json.dumps(CHINESE, indent=2, ensure_ascii=False))


@cli.command()
@click.argument('src')
@click.option('--file', default='', help='Dict file to update.', type=str)
@click.option('--skip', default='',
              help='skip dir or file, please split with ",".', type=str)
@click.option('--skipexts', default='',
              help='skip extensions,  please split with ",".', type=str)
@click.option('--onlyexts', default='',
              help='only extensions, please split with ",".', type=str)
@click.option('--one', default=False,
              help='one file, not dir.', type=bool)
def replace(src, file, skip, skipexts, onlyexts, one):
    if file:
        with open(file, 'rb') as f:
            kv = json.load(f, 'utf-8')
    if one:
        if not os.path.isfile(src):
            raise Exception('{} not a file.'.format(src))
        read(src, kv=kv)
    else:
        handle_dir(src, skip, skipexts, onlyexts, kv=kv)

if __name__ == '__main__':
    cli()
