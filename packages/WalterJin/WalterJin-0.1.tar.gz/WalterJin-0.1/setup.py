###
# python setup.py sdist
# python setup.py sdist bdist_wheel
# easy_install xxx.tar.gz
# pip install -U example_package.whl
# ##

import PIL
from setuptools import setup, find_packages

setup(
    name='WalterJin',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "pillow==10.2.0",
        "oracledb==2.0.1",
        "json5==0.9.14"
    ],
)