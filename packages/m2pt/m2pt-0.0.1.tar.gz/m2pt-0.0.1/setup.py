# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['m2pt']

package_data = \
{'': ['*']}

install_requires = \
['swarms', 'zetascale']

setup_kwargs = {
    'name': 'm2pt',
    'version': '0.0.1',
    'description': 'M2PT - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Multi-Modal Pathway Transformer\nImplementation of M2PT in PyTorch from the paper: "Multimodal Pathway: Improve Transformers with Irrelevant Data from Other Modalities".  [PAPER LINK](https://arxiv.org/abs/2401.14405)\n\n\n## Install\n\n\n## Citation\n```bibtex\n@misc{zhang2024multimodal,\n    title={Multimodal Pathway: Improve Transformers with Irrelevant Data from Other Modalities}, \n    author={Yiyuan Zhang and Xiaohan Ding and Kaixiong Gong and Yixiao Ge and Ying Shan and Xiangyu Yue},\n    year={2024},\n    eprint={2401.14405},\n    archivePrefix={arXiv},\n    primaryClass={cs.CV}\n}\n```\n\n\n# License\nMIT\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/M2PT',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
