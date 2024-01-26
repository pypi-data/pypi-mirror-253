# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mambabyte']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'mambabyte',
    'version': '0.0.2',
    'description': 'MambaByte - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n\n# MambaByte\nImplementation of MambaByte in "MambaByte: Token-free Selective State Space Model" in Pytorch and Zeta. Note this will be a higher performance implementation of Mamba with parallel scan \n\n\n## Installation\n\n```bash\npip install mambabyte\n```\n\n# Usage\n```python\nimport torch \nfrom mambabyte import MambaConfig, Mamba\n\nx = torch.randn(2, 3, 4)\nconfig = MambaConfig(\n    dim = 4,\n    depth = 3,\n    dt_rank = 2,\n    d_state = 2,\n    expand_factor = 2,\n    d_conv = 3,\n    dt_min = 0.001,\n    dt_max = 0.1,\n    dt_init = "random",\n    dt_scale = 1.0,\n    bias = False,\n    conv_bias = True,\n    pscan = True\n)\n\nmodel = Mamba(config)\n\nout = model(x)\n\nprint(out)\n\n```\n\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/MambaByte',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
