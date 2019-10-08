import os
import sys
import json

import click


class Json:
    def __init__(self, filename):
        self.filename = filename
        # self.json = None
        with open(filename, 'r') as fp:
            self.json = json.load(fp)

    def set(self, key, value):
        self.json[key] = value

    def get(self, key):
        return self.json.get(key)

    def list(self):
        return self.json.keys()

    def flush(self):
        with open(self.filename, 'w') as fp:
            json.dump(self.json, fp)


def get_json():
    db_path = os.environ.get('TOY_DB')
    if not db_path:
        print('Please set the TOY_DB environment variable.')
        sys.exit(0)

    return Json(db_path)


@click.group()
def snip():
    """Snip tools."""
    pass


@snip.command()
# @click.argument('key')
def keys():
    db = get_json()
    for key in db.list():
        print(key)


@snip.command()
@click.argument('key')
def get(key):
    db = get_json()
    print(db.get(key))


@snip.command()
@click.argument('key')
@click.argument('value')
def set(key, value):
    db = get_json()
    db.set(key, value)
    db.flush()
