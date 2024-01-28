# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['whecho']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1', 'setuptools>=40.6.3', 'toml>=0.6.0']

entry_points = \
{'console_scripts': ['whecho = whecho:whecho.main']}

setup_kwargs = {
    'name': 'whecho',
    'version': '0.0.3',
    'description': 'Linux echo with webhooks! ⚓',
    'long_description': '# whecho\nlinux echo but with webhooks! ⚓\n\nDon\'t guess when a job is finished! Have it message you!\n\n## requirements\n- python 3.6+\n\n## installation\n```\npip install whecho\n```\n\n## First Time Setup\n- obtain a webhook URL\n![discord_webhook_example](https://i.imgur.com/f9XnAew.png)\n\n```\n$ whecho --init\nCurrent config:\n[1] default_url: None\n[2] user: craut\n[3] machine: craut-spectre\n\nPlease enter the number/name of the config option you would like to modify (empty or Q to exit): 1\nPlease enter the new value for default_url: <WEBHOOK_URL>\nSuccessfully modified default_url to <WEBHOOK_URL>!\nCurrent config:\n[1] default_url: <WEBHOOK_URL>\n[2] user: craut\n[3] machine: craut-spectre\n\nPlease enter the number/name of the config option you would like to modify (empty or Q to exit): q\nSuccessfully initialized whecho!\n```\n\n## general usage (from shell/console)\n```\n$ whecho "hello there"\n```\n![hello_there_discord](https://github.com/cvraut/whecho/blob/main/imgs/hello_there_discord.png?raw=true)',
    'author': 'Chinmay Raut',
    'author_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
