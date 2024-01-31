# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nornir_pyez',
 'nornir_pyez.plugins',
 'nornir_pyez.plugins.connections',
 'nornir_pyez.plugins.tasks']

package_data = \
{'': ['*']}

install_requires = \
['junos-eznc>=2.5,<3.0', 'nornir>=3.0.0', 'xmltodict==0.12.0']

entry_points = \
{'nornir.plugins.connections': ['pyez = nornir_pyez.plugins.connections:Pyez']}

setup_kwargs = {
    'name': 'nornir-pyez',
    'version': '0.2.9',
    'description': 'PyEZ Plugin for Nornir',
    'long_description': 'None',
    'author': 'Knox Hutchinson',
    'author_email': 'knox@knoxsdata.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
