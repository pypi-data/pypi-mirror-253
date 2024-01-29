# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['morpheus_torch']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'morpheus-torch',
    'version': '0.0.7',
    'description': 'Morpheus - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Morpheus 1\n\n![Morphesus transformer](morpheus.jpeg)\n\nImplementation of "MORPHEUS-1" from Prophetic AI and "The world’s first multi-modal generative ultrasonic transformer designed to induce and stabilize lucid dreams. "\n\n\n\n\n\n## Installation\n\n```bash\npip install morpheus-torch\n```\n\n# Usage\n- The input is FRMI and EEG tensors.\n\n- FRMI shape is (batch_size, in_channels, D, H, W)\n\n- EEG Embedding is [batch_size, channels, time_samples]\n\n```python\n# Importing the torch library\nimport torch\n\n# Importing the Morpheus model from the morpheus_torch package\nfrom morpheus_torch.model import Morpheus\n\n# Creating an instance of the Morpheus model with specified parameters\nmodel = Morpheus(\n    dim=128,  # Dimension of the model\n    heads=4,  # Number of attention heads\n    depth=2,  # Number of transformer layers\n    dim_head=32,  # Dimension of each attention head\n    dropout=0.1,  # Dropout rate\n    num_channels=32,  # Number of input channels\n    conv_channels=32,  # Number of channels in convolutional layers\n    kernel_size=3,  # Kernel size for convolutional layers\n    in_channels=1,  # Number of input channels for convolutional layers\n    out_channels=32,  # Number of output channels for convolutional layers\n    stride=1,  # Stride for convolutional layers\n    padding=1,  # Padding for convolutional layers\n    ff_mult=4,  # Multiplier for feed-forward layer dimension\n    scatter = False, # Whether to scatter to 4d representing spatial dimensions\n)\n\n# Creating random tensors for input data\nfrmi = torch.randn(1, 1, 32, 32, 32)  # Random tensor for FRMI data\neeg = torch.randn(1, 32, 128)  # Random tensor for EEG data\n\n# Passing the input data through the model to get the output\noutput = model(frmi, eeg)\n\n# Printing the shape of the output tensor\nprint(output.shape)\n\n\n```\n\n\n\n### Code Quality 🧹\n\n- `make style` to format the code\n- `make check_code_quality` to check code quality (PEP8 basically)\n- `black .`\n- `ruff . --fix`\n\n# License\nMIT\n\n# Todo\n- [ ] Implement the scatter in the end of the decoder to output spatial outputs which are 4d?\n\n- [x] Implement a full model with the depth of the decoder layers\n\n- [ ] Change all the MHAs to Multi Query Attentions\n\n- [ ] Double check popular brain scan EEG and FRMI AI papers to double check tensor shape\n\n',
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
