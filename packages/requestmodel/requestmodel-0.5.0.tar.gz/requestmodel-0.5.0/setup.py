# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['requestmodel', 'requestmodel.adapters']

package_data = \
{'': ['*']}

install_requires = \
['fastapi', 'httpx']

setup_kwargs = {
    'name': 'requestmodel',
    'version': '0.5.0',
    'description': 'requestmodel',
    'long_description': "# requestmodel\n\n[![PyPI](https://img.shields.io/pypi/v/requestmodel.svg)][pypi status]\n[![Status](https://img.shields.io/pypi/status/requestmodel.svg)][pypi status]\n[![Python Version](https://img.shields.io/pypi/pyversions/requestmodel)][pypi status]\n[![License](https://img.shields.io/pypi/l/requestmodel)][license]\n\n[![Read the documentation at https://requestmodel.readthedocs.io/](https://img.shields.io/readthedocs/requestmodel/latest.svg?label=Read%20the%20Docs)][read the docs]\n[![Tests](https://github.com/foarsitter/requestmodel/workflows/Tests/badge.svg)][tests]\n[![Codecov](https://codecov.io/gh/foarsitter/requestmodel/branch/main/graph/badge.svg)][codecov]\n\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]\n\n[pypi status]: https://pypi.org/project/requestmodel/\n[read the docs]: https://requestmodel.readthedocs.io/\n[tests]: https://github.com/foarsitter/requestmodel/actions?workflow=Tests\n[codecov]: https://app.codecov.io/gh/foarsitter/requestmodel\n[pre-commit]: https://github.com/pre-commit/pre-commit\n[black]: https://github.com/psf/black\n\n## Features\n\n- Model your http requests as a pydantic model\n- Annotate your request parameters with fastapi params\n- Support voor sync & async requests\n\n## Goals\n\n- Create a generator for an OpenAPI spec\n- Support all kinds of http requests\n\n## Installation\n\nYou can install _requestmodel_ via [pip] from [PyPI]:\n\n```console\n$ pip install requestmodel\n```\n\n## Usage\n\nPlease see the [implementation detail] for further instructions.\n\n## Contributing\n\nContributions are very welcome.\nTo learn more, see the [Contributor Guide].\n\n## License\n\nDistributed under the terms of the [MIT license][license],\n_requestmodel_ is free and open source software.\n\n## Issues\n\nIf you encounter any problems,\nplease [file an issue] along with a detailed description.\n\n## Credits\n\nThis project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.\n\n[@cjolowicz]: https://github.com/cjolowicz\n[pypi]: https://pypi.org/\n[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n[file an issue]: https://github.com/foarsitter/requestmodel/issues\n[pip]: https://pip.pypa.io/\n\n<!-- github-only -->\n\n[license]: https://github.com/foarsitter/requestmodel/blob/main/LICENSE\n[contributor guide]: https://github.com/foarsitter/requestmodel/blob/main/CONTRIBUTING.md\n[implementation detail]: https://requestmodel.readthedocs.io/en/latest/usage.html\n",
    'author': 'Jelmer Draaijer',
    'author_email': 'info@jelmert.nl',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/foarsitter/requestmodel',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
