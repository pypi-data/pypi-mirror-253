# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['grooper', 'grooper.core', 'grooper.exceptions', 'grooper.utils']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.31.0,<3.0.0']

setup_kwargs = {
    'name': 'grooper',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Python Grooper Wrapper\n\nThis wrapper encapsulates the functionality provided in the grooper API.\n\n## Usage\n\n```python\nimport grooper.core import API, Batch\n\nAPI.key = <API Key>\nAPI.url = <API URL>\n\nbatch = Batch.find(<Batch ID>)\nprint(batch)\n```\n\n## Testing\n\nTo run the tests, you need to have `pytest` and `coverage` installed. To run the tests and generate a coverage report, run the following commands:\n\n```bash\ncoverage run --source=. -m pytest\ncoverage report\n```\n\nBefore committing, make sure you are styling appropriately your code. For that, you can run the following command (assuming you have installed `black`, `isort` and `pylint`):\n\n```bash\nblack .\nisort .\npylint grooper tests\n```\n',
    'author': 'Adrian Carreno',
    'author_email': 'adrian.carreno@gomoder.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
