# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hartware_lib',
 'hartware_lib.adapters',
 'hartware_lib.commands',
 'hartware_lib.controllers',
 'hartware_lib.serializers',
 'hartware_lib.utils']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.8.0,<0.9.0',
 'pyyaml>=6.0.1,<7.0.0',
 'requests-mock>=1.9.3,<2.0.0',
 'types-requests>=2.27.16,<3.0.0']

extras_require = \
{'all': ['aiohttp>=3.8.3,<4.0.0',
         'aio-pika>=9.3.1,<10.0.0',
         'slack-sdk>=3.11.2,<4.0.0',
         'pandas>=2.1.4,<3.0.0',
         'numpy>=1.26.3,<2.0.0'],
 'async-http': ['aiohttp>=3.8.3,<4.0.0'],
 'async-rabbitmq': ['aio-pika>=9.3.1,<10.0.0'],
 'data-science': ['pandas>=2.1.4,<3.0.0', 'numpy>=1.26.3,<2.0.0'],
 'slack': ['slack-sdk>=3.11.2,<4.0.0']}

entry_points = \
{'console_scripts': ['slack_send = hartware_lib.commands.slack:slack_send']}

setup_kwargs = {
    'name': 'hartware-lib',
    'version': '0.5.12',
    'description': 'Core helper lib for Hartware codes.',
    'long_description': '# Hartware Lib\n',
    'author': 'Laurent Arthur',
    'author_email': 'laurent.arthur75@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/ludwig778/python-lib',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
