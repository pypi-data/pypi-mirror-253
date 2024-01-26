# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['morpheus_torch']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'swarms', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'morpheus-torch',
    'version': '0.0.1',
    'description': 'Morpheus - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Morpheus 1\n![Morphesus transformer](morpheus.jpeg)\nImplementation of "MORPHEUS-1" from Prophetic AI and "The world’s first multi-modal generative ultrasonic transformer designed to induce and stabilize lucid dreams. "\n\n\n\n\n\n## Installation\n\nYou can install the package using pip\n\n```bash\npip install -e .\n```\n\n# Usage\n```python\n\n```\n\n\n\n### Code Quality 🧹\n\nWe providehandy commands inside the `Makefile`, namely:\n\n- `make style` to format the code\n- `make check_code_quality` to check code quality (PEP8 basically)\n- `black .`\n- `ruff . --fix`\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/MORPHEUS-1',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
