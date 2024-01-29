# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['djx_account',
 'djx_account.management',
 'djx_account.management.commands',
 'djx_account.migrations',
 'djx_account.serializers',
 'djx_account.services',
 'djx_account.signals',
 'djx_account.tests',
 'djx_account.utils',
 'djx_account.views']

package_data = \
{'': ['*'],
 'djx_account': ['templates/header/*',
                 'templates/password_reset/*',
                 'templates/registration_welcome/*',
                 'templates/user_confirmation/*']}

install_requires = \
['django>=4.1.4,<6.0',
 'djangorestframework-simplejwt>=5.2.2,<6.0.0',
 'djangorestframework>=3.14.0,<4.0.0',
 'facebook-sdk>=3.1.0,<4.0.0',
 'google-auth>=2.15.0,<3.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'msal>=1.20.0,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tweepy>=4.12.1,<5.0.0']

setup_kwargs = {
    'name': 'djx-account',
    'version': '0.1.6',
    'description': '',
    'long_description': '',
    'author': 'nope',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
