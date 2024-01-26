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
    'version': '0.0.4',
    'description': 'Morpheus - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Morpheus 1\n\n![Morphesus transformer](morpheus.jpeg)\n\nImplementation of "MORPHEUS-1" from Prophetic AI and "The world’s first multi-modal generative ultrasonic transformer designed to induce and stabilize lucid dreams. "\n\n\n\n\n\n## Installation\n\nYou can install the package using pip\n\n```bash\npip install morpheus-torch\n```\n\n# Usage\n- The input is FRMI and EEG tensors.\n\n- FRMI shape is (batch_size, in_channels, D, H, W)\n\n- EEG Embedding is [batch_size, channels, time_samples]\n\n```python\nimport torch\n\nfrom morpheus_torch import MorpheusDecoder\n\nmodel = MorpheusDecoder(\n    dim=128,\n    heads=4,\n    depth=2,\n    dim_head=32,\n    dropout=0.1,\n    num_channels=32,\n    conv_channels=32,\n    kernel_size=3,\n    in_channels=1,\n    out_channels=32,\n    stride=1,\n    padding=1,\n    ff_mult=4,\n)\n\nfrmi = torch.randn(1, 1, 32, 32, 32)\neeg = torch.randn(1, 32, 128)\n\noutput = model(frmi, eeg)\nprint(output.shape)\n\n\n```\n\n\n\n### Code Quality 🧹\n\nWe providehandy commands inside the `Makefile`, namely:\n\n- `make style` to format the code\n- `make check_code_quality` to check code quality (PEP8 basically)\n- `black .`\n- `ruff . --fix`\n\n# License\nMIT\n\n# Todo\n- [ ] Implement the scatter in the end of the decoder to output spatial outputs\n\n- [ ] Implement a full model with the depth of the decoder layers\n\n- [ ] Change all the MHAs to Multi Query Attentions\n\n- [ ] Double check popular brain scan EEG and FRMI AI papers to double check tensor shape\n\n',
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
