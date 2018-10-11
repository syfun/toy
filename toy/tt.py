import time

import click

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


@click.group()
def tt():
    """Unix timestamp and Time string convert each other."""
    pass


@tt.command()
@click.argument('timestamp')
@click.option('--fmt', '-F', default=TIME_FORMAT,
              help='Format for time, default is %Y-%m-%d %H:%M:%S, like 2000-10-01 01:23:45')
def t2s(timestamp, fmt):
    """Unix timestamp => Time string"""
    t = time.localtime(int(timestamp))
    print(time.strftime(fmt, t))


@tt.command()
@click.option('--string', '-S', default='', help='time string')
@click.option('--fmt', '-F', default=TIME_FORMAT,
              help='Format for time, default is %Y-%m-%d %H:%M:%S, like 2000-10-01 01:23:45')
def s2t(string, fmt):
    """Time string => Unix timestamp"""
    if string == '':
        print(int(time.time()))
    else:
        t = time.strptime(string, fmt)
        print(int(time.mktime(t)))
