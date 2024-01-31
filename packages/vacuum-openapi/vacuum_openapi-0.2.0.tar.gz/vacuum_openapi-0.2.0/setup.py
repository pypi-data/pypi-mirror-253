# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vacuum', 'vacuum.lib']

package_data = \
{'': ['*']}

install_requires = \
['orjson>2.2.0,<4.0.0', 'pydantic>1.8.0,<3.0.0']

setup_kwargs = {
    'name': 'vacuum-openapi',
    'version': '0.2.0',
    'description': 'Python bindings for the vacuum OpenAPI linting/validation Go library',
    'long_description': '# vacuum-python',
    'author': 'Zach Kanzler',
    'author_email': 'they4kman@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}
from build_wheels import *
build(setup_kwargs)

setup(**setup_kwargs)
