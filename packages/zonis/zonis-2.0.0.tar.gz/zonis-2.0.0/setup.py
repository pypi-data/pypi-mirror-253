# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zonis']

package_data = \
{'': ['*']}

install_requires = \
['websockets>=10.4,<11.0']

setup_kwargs = {
    'name': 'zonis',
    'version': '2.0.0',
    'description': 'Agnostic IPC for Python programs ',
    'long_description': 'Zonis\n---\n\nA coro based callback system for many to one IPC setups.\n\n`pip install zonis`\n\n\n=======\nSee the [examples](https://github.com/Skelmis/Zonis/tree/master/examples) for simple use cases.\n___\n\n## Build the docs locally\n\nIf you want to build and run the docs locally using sphinx run\n```\nsphinx-autobuild -a docs docs/_build/html --watch zonis\n```\n\nthis will build the docs and start a local server; additionally it will listed for changes to the source directory ``zonis`` and to the docs source directory ``docs/``.\nYou can find the builded files at ``docs/_build``.\n',
    'author': 'skelmis',
    'author_email': 'skelmis.craft@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
