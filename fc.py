# coding=utf-8
"""
Example:
    python fc.py ./src --skipexts="jpg,jpeg,png,ico,svg" --onlyexts="html"
    python fc.py ./login.html --one true
"""

import codecs
import json
import os
import re

import click
from scandir import scandir

P = re.compile(u'[\u4e00-\u9fff]+')
CHINESE = {}


def read(filename):
    print(filename)
    with open(filename, 'r') as f:
        for line in f.readlines():
            # print line
            m = P.findall(line.decode('utf-8'))
            if m:
                for i in m:
                    CHINESE[i] = ""


def handle_dir(dirname, skip, skipexts, onlyexts):
    if not os.path.isdir(dirname):
        raise Exception('{} not a directory.'.format(dirname))
    for entry in scandir(dirname):
        if entry.name in skip:
            continue
        if '.' in entry.name:
            ext = entry.name.split('.')[1]
            if ext not in onlyexts:
                continue
            if ext in skipexts:
                continue
        if entry.is_file():
            read(entry.path)
        elif entry.is_dir():
            handle_dir(entry.path, skip, skipexts, onlyexts)


@click.command()
@click.argument('src')
@click.option('--skip', default='',
              help='skip dir or file, please split with ",".', type=str)
@click.option('--skipexts', default='',
              help='skip extensions,  please split with ",".', type=str)
@click.option('--onlyexts', default='',
              help='only extensions, please split with ",".', type=str)
@click.option('--one', default=False,
              help='one file, not dir.', type=bool)
def find_chinese(src, skip, skipexts, onlyexts, one):
    if one:
        if not os.path.isfile(src):
            raise Exception('{} not a file.'.format(src))
        read(src)
    else:
        handle_dir(src, skip, skipexts, onlyexts)
    with codecs.open('out.json', 'w', 'utf-8') as f:
        f.write(json.dumps(CHINESE, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    find_chinese()
