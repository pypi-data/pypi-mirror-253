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
    'version': '0.0.1',
    'description': 'MambaByte - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n\n# MambaByte\nImplementation of MambaByte in "MambaByte: Token-free Selective State Space Model" in Pytorch and Zeta. Note this will be a higher performance implementation of Mamba with parallel scan \n\n\n## Installation\n\n```bash\npip install mambabyte\n```\n\n# Usage\n```python\n\n```\n\n\n# License\nMIT\n',
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
