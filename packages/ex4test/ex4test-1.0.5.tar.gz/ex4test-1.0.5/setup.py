# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ex4test']

package_data = \
{'': ['*']}

install_requires = \
['nicegui>=1.4.12,<2.0.0']

setup_kwargs = {
    'name': 'ex4test',
    'version': '1.0.5',
    'description': '',
    'long_description': '# my-libs',
    'author': 'CrystalWindSnake',
    'author_email': '568166495@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
