"""
Toy for day.

Some useable tools, such as timestamp convert to time string.
"""

import os
from setuptools import setup, find_packages


def get_version():
    version = os.environ.get('VERSION', 'dev')
    with open('toy/__init__.py', 'r+') as f:
        c = f.read()
        c = c.replace('DEV_VERSION', version)
        f.seek(0, 0)
        f.truncate()
        f.write(c)
    return version


def get_requirements():
    with open('requirements.txt') as requirements:
        return [line.strip() for line in requirements
                if line and not line.startswith(('#', '--'))]


setup(
    name='Toy',
    version=os.environ.get('VERSION', 'dev'),
    url='https://github.com/syfun/toy',
    author='YungSung',
    author_email='sunyu418@gmail.com',
    description=__doc__,
    long_description=__doc__,
    packages=find_packages(exclude=["tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=get_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Private :: Do Not Upload'
    ],
    entry_points='''
        [console_scripts]
        toy=toy.cli:main
    '''
)