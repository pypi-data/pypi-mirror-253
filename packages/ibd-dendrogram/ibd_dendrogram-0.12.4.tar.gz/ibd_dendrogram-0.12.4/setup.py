# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ibd_dendrogram']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.1,<4.0.0',
 'numpy>=1.22.2,<2.0.0',
 'pandas>=1.4.1,<2.0.0',
 'scipy>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'ibd-dendrogram',
    'version': '0.12.4',
    'description': 'module that helps to form a dendrogram',
    'long_description': '[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![PyPI version](https://badge.fury.io/py/ibd_dendrogram.svg)](https://badge.fury.io/py/ibd_dendrogram)\n[![Documentation Status](https://readthedocs.org/projects/ibd-dendrogram/badge/?version=latest)](https://ibd-dendrogram.readthedocs.io/en/latest/?badge=latest)\n\n# ibd-dendrogram:\n\nA python module to help users create a distance matrix and construct a dendrogram using Identity by Descent segments as a distance marker. The default distance is calculated as 1/(shared ibd segment length). Documentation explaining the api can be found here: [ibd-dendrogram docs](https://ibd-dendrogram.readthedocs.io/en/latest/) \n\nThis module has four accessible methods: make_distance_matrix, record_matrix, generate_dendrogram, draw_dendrogram.\n\n',
    'author': 'jtb',
    'author_email': 'james.baker@vanderbilt.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jtb324/ibd_dendrogram',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
