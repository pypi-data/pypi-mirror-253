# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spacestar']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'Markdown>=3.5.2,<4.0.0',
 'hx-markup>=0.2.2,<0.3.0',
 'itsdangerous>=2.1.2,<3.0.0',
 'ormspace>=0.3.0,<0.4.0',
 'python-multipart>=0.0.6,<0.0.7',
 'starlette>=0.32.0,<0.33.0',
 'uvicorn>=0.24.0,<0.25.0']

entry_points = \
{'console_scripts': ['init-static = '
                     'spacestar.initfolders:create_static_directory',
                     'init-templates = '
                     'spacestar.initfolders:create_templates_directory',
                     'initfolders = spacestar.initfolders:main']}

setup_kwargs = {
    'name': 'spacestar',
    'version': '0.2.8',
    'description': 'Framework for building web based apps with the power of Starlette, Pydantic and Deta Space.',
    'long_description': None,
    'author': 'Daniel Arantes',
    'author_email': 'arantesdv@me.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
