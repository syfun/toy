# coding=utf-8

import time

import click

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

@click.group()
def cli():
    pass


@click.command()
@click.argument('timestamp')
def t2s(timestamp):
    t = time.localtime(int(timestamp))
    print time.strftime(TIME_FORMAT, t)


@click.command()
@click.argument('string')
def s2t(string):
    t = time.strptime(string, TIME_FORMAT)
    print int(time.mktime(t))


if __name__ == '__main__':
    cli.add_command(t2s)
    cli.add_command(s2t)
    cli()


