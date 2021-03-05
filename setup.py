from setuptools import setup
from cicdtest import __version__
import os
import re


def read_meta():
    """Read each of the keys stored in __init__.py

    Returns
    -------
    dict[str, str]
        A dictionary containing each of the string key value pairs.
    """
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'cicdtest/__init__.py')
    with open(path) as fh:
        hits = re.findall(r'__(\w+)__ ?= ?["\'](.+)["\']\n', fh.read())
    return {k: v for k, v in hits}

meta = read_meta()

setup(name='foobartestignore',
      version=meta['version'],
      python_requires='>=3.6',
      )
