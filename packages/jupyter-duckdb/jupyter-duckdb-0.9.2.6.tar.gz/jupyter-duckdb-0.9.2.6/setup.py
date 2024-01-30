import os
import re
from datetime import datetime

from setuptools import setup, find_packages

# version
version = os.getenv('PACKAGE_VERSION', '1.0')
version = re.sub(r'[^dev0-9._]', '', version)

# install requires
install_requires = [
    'jupyter',
    'graphviz==0.20.1',
    'checkmarkandcross'
]

if os.getenv('SQLITE') != '1':
    install_requires += ['duckdb==0.9.2']

# load README.md as long_description
with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

# main setup call
setup(
    name='jupyter-duckdb',
    version=version,
    author='Eric Tröbs',
    author_email='eric.troebs@tu-ilmenau.de',
    description='a basic wrapper kernel for DuckDB',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erictroebs/jupyter-duckdb',
    project_urls={
        'Bug Tracker': 'https://github.com/erictroebs/jupyter-duckdb/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.10',
    install_requires=install_requires,
    package_data={
        'duckdb_kernel': [
            'kernel.json',
            'db/implementation/duckdb/*.py',
            'db/implementation/postgres/*.py',
            'db/implementation/sqlite/*.py'
        ]
    },
    include_package_data=True
)
