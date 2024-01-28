# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deepvelo',
 'deepvelo.base',
 'deepvelo.data_loader',
 'deepvelo.logger',
 'deepvelo.model',
 'deepvelo.pipeline',
 'deepvelo.plot',
 'deepvelo.tool',
 'deepvelo.trainer',
 'deepvelo.utils']

package_data = \
{'': ['*']}

install_requires = \
['adjustText>=0.7.3,<0.8.0',
 'hnswlib>=0.6.2,<0.7.0',
 'igraph>=0.9.10,<0.10.0',
 'matplotlib>=3.3,<3.6',
 'numpy>=1.21.1,<2.0.0',
 'scanpy>=1.8.2,<2.0.0',
 'scvelo>=0.2.4,<0.3.0',
 'seaborn>=0.11.2,<0.12.0',
 'torch>=1.2,<1.13',
 'tqdm>=4.62.3,<5.0.0',
 'umap-learn>=0.5.2,<=0.5.4']

extras_require = \
{'gpu': ['dgl-cu102>=0.4,!=0.8.0.post1,<0.9']}

setup_kwargs = {
    'name': 'deepvelo',
    'version': '0.2.8',
    'description': 'Deep Velocity',
    'long_description': '# DeepVelo - A Deep Learning-based velocity estimation tool with cell-specific kinetic rates\n\n[![PyPI version](https://badge.fury.io/py/deepvelo.svg)](https://badge.fury.io/py/deepvelo)\n[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n\nThis is the official implementation of the [DeepVelo](https://www.biorxiv.org/content/10.1101/2022.04.03.486877) method.\nDeepVelo employs cell-specific kinetic rates and provides more accurate RNA velocity estimates for complex differentiation and lineage decision events in heterogeneous scRNA-seq data. Please check out the paper for more details.\n\n![alt text](https://user-images.githubusercontent.com/11674033/171066682-a899377f-fae1-452a-8b67-8bc8c244b641.png)\n\n## Installation\n\n```bash\npip install deepvelo\n```\n\n### Using GPU\n\nThe `dgl` cpu version is installed by default. For GPU acceleration, please install a proper [dgl gpu](https://www.dgl.ai/pages/start.html) version compatible with your CUDA environment.\n\n```bash\npip uninstall dgl # remove the cpu version\n# replace cu101 with your desired CUDA version and run the following\npip install "dgl-cu101>=0.4.3,<0.7"\n\n```\n\n### Install the development version\n\nWe use poetry to manage dependencies.\n\n```bash\npoetry install\n```\n\nThis will install the exact versions in the provided [poetry.lock](poetry.lock) file. If you want to install the latest version for all dependencies, use the following command.\n\n```bash\npoetry update\n```\n\n## Usage\n\nWe provide a number of notebooks in the [exmaples](examples) folder to help you get started. DeepVelo fullly integrates with [scanpy](https://scanpy.readthedocs.io/en/latest/) and [scVelo](https://scvelo.readthedocs.io/). The basic usage is as follows:\n\n```python\nimport deepvelo as dv\nimport scvelo as scv\n\nadata = ... # load your data in AnnData format\n\n# preprocess the data\nscv.pp.filter_and_normalize(adata, min_shared_counts=20, n_top_genes=2000)\nscv.pp.moments(adata, n_neighbors=30, n_pcs=30)\n\n# run DeepVelo using the default configs\ntrainer = dv.train(adata, dv.Constants.default_configs)\n# this will train the model and predict the velocity vectore. The result is stored in adata.layers[\'velocity\']. You can use trainer.model to access the model.\n```\n\n### Fitting large number of cells\n\nIf you can not fit a large dataset into (GPU) memory using the default configs, please try setting a small `inner_batch_size` in the configs, which can reduce the memory usage and maintain the same performance.\n\nCurrently the training works on the whole graph of cells, we plan to release a flexible version using graph node sampling in the near future.\n',
    'author': 'subercui',
    'author_email': 'subercui@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bowang-lab/DeepVelo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
