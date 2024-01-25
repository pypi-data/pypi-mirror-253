# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['odometer']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'odometer',
    'version': '0.1.0',
    'description': 'odometer classes',
    'long_description': '# Odometer\n\n[![image](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)[![image](https://readthedocs.org/projects/odometer/badge/?version=latest)](https://odometer.readthedocs.io/en/latest/?badge=latest)[![image](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)[![image](https://img.shields.io/badge/semantic--release-angular-e10079?logo=semantic-release)](https://github.com/python-semantic-release/python-semantic-release)[![image](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)[![image](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)[![image](http://www.mypy-lang.org/static/mypy_badge.svg)](https://github.com/python/mypy)[![image](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![image](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)\n\nAccording to Wikipedia:\n: An *odometer* or *odograph* is an instrument used for measuring the distance traveled by a vehicle, such as a bicycle or car. The device may be electronic, mechanical, or a combination of the two. The noun derives from ancient Greek **ὁδόμετρον**, **hodómetron**, from **ὁδός**, **hodós** and **μέτρον**, **métron**.\n\nWhen you take a look at how it behaves, you come up with the following:\n\n> - a sequence of *displays*\n>   > - each individual *display* show a *value* from a *predefined list of ordered values*\n>   > - the displayed value *rotates* over the predefined list of ordered values\n>   >   > - each full rotation of a *display* affects the rotation of its neighbour\n\nThe predefined list of ordered values in a traditional odometer is composed of the decimal digits 0 to 9.\nHowever this list can technically be anything you want it to be:\n\n> - characters\n> - words\n> - names of days of the week\n> - months\n> - …\n\nIt is exactly that kind of functionality odometer aim to provide.\n\n## Installation\n\n### Requirements\n\nSee [Requirements for Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-requirements) for\ninstructions on how to install python packages in general.\n\n### Installing from PyPI\n\nTo install the latest version of odometer:\n\nUnix/macOS\n\n```bash\npython3 -m pip install odometer\n```\n\nWindows\n\n```bat\npy -m pip install odometer\n```\n\nTo install a specific version:\n\nUnix/macOS\n\n```bash\npython3 -m pip install odometer==1.4\n```\n\nWindows\n\n```bat\npy -m pip install odometer==1.4\n```\n\nTo install greater than or equal to one version and less than another:\n\nUnix/macOS\n\n```bash\npython3 -m pip install odometer>=1,<2\n```\n\nWindows\n\n```bat\npy -m pip install odometer>=1,<2\n```\n\nTo install a version that’s [compatible](https://packaging.python.org/en/latest/specifications/version-specifiers/#version-specifiers-compatible-release)\nwith a certain version: \n\nUnix/macOS\n\n```bash\npython3 -m pip install odometer~=1.4.2\n```\n\nWindows\n\n```bat\npy -m pip install odometer~=1.4.2\n```\n\nIn this case, this means to install any version “==1.4.\\*” version that’s also\n“>=1.4.2”.\n\n## Documentation\n\nYou can find read the latest documentation at [Read The Docs](https://odometer.readthedocs.io/en/latest/)\n\n## License\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the [Free Software Foundation](https://www.fsf.org/), either version 3 of the License, or (at your option) any later version.\n\n[![image](https://static.fsf.org/common/img/logo-new.png)](https://www.fsf.org/)\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License  along with this program. If not, see [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html).\n\n[![image](https://www.gnu.org/graphics/gplv3-or-later.svg)](https://www.gnu.org/licenses/gpl-3.0.en.html)\n',
    'author': 'An0nym0u5',
    'author_email': 'anonym0u5@disroot.org',
    'maintainer': 'An0nym0u5',
    'maintainer_email': 'anonym0u5@disroot.org',
    'url': 'https://gitlab.com/Anonym0u5/odometer',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
