import os
from setuptools import setup
from knowl_apidocs.version import VERSION

NAME = "knowl_apidocs"
VERSION = ''.join([char for char in VERSION if not char.isspace()])

setup(
    name=NAME,
    version=VERSION,
    url="https://github.com/knowl-doc/APIDocs",
    entry_points={
        'console_scripts': [
            'knowl_apidocs = knowl_apidocs.apidocs:main'
        ]
    },
)