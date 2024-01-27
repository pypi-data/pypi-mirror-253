# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neurobench',
 'neurobench.benchmarks',
 'neurobench.datasets',
 'neurobench.models',
 'neurobench.postprocessing',
 'neurobench.preprocessing']

package_data = \
{'': ['*']}

install_requires = \
['llvmlite>=0.40.1,<0.41.0',
 'numba>=0.57.1,<0.58.0',
 'numpy>=1.24.3,<2.0.0',
 'snntorch>=0.7.0,<0.8.0',
 'tonic>=1.4.0,<2.0.0',
 'torch>=2.0.1,<3.0.0',
 'torchaudio>=2.0.2,<3.0.0',
 'tqdm>=4.65.0,<5.0.0']

extras_require = \
{'mackey-glass': ['jitcdde>=1.8.1,<2.0.0'],
 'nehar': ['pytorch-lightning>=1.4.0,<2.0.0', 'gdown>=4.7.1,<5.0.0']}

setup_kwargs = {
    'name': 'neurobench',
    'version': '1.0.2',
    'description': 'Collaborative, Fair, and Representative Benchmarks for Neuromorphic Computing',
    'long_description': "============\nIntroduction\n============\n\nA harness for running evaluations on\n`NeuroBench <https://neurobench.ai>`__ algorithm benchmarks.\n\nNeuroBench is a community-driven project, and we welcome further\ndevelopment from the community. If you are interested in developing\nextensions to features, programming frameworks, or metrics and tasks,\nplease see the `Contributing Guidelines <https://neurobench.readthedocs.io/en/latest/contributing.html>`__.\n\nNeuroBench Structure\n---------------------\n\nNeuroBench contains the following sections:\n\n.. list-table:: \n   :widths: 20 60\n\n   * - **Section**\n     - **Description**\n   * - `neurobench.benchmarks <https://neurobench.readthedocs.io/en/latest/neurobench.benchmarks.html>`__\n     - Neurobench benchmarks, including data metrics and static metrics\n   * - `neurobench.datasets <https://neurobench.readthedocs.io/en/latest/neurobench.datasets.html>`__\n     - Neurobench benchmark datasets\n   * - `neurobench.models <https://neurobench.readthedocs.io/en/latest/neurobench.models.html>`__\n     - Neurobench framework for Torch and SNNTorch models\n   * - `neurobench.preprocessing <https://neurobench.readthedocs.io/en/latest/neurobench.preprocessing.html>`__\n     - Pre-processing of data, conversion to spikes\n   * - `neurobench.postprocessing <https://neurobench.readthedocs.io/en/latest/neurobench.postprocessing.html>`__\n     - Post-processors take the spiking output from the models and provide several methods of combining them\n\nInstallation\n------------\n\nInstall from PyPI:\n\n::\n\n   pip install neurobench\n\nBenchmarks\n----------\n\nThe following benchmarks are currently available:\n\nv1.0 benchmarks\n~~~~~~~~~~~~~~~\n- Keyword Few-shot Class-incremental Learning (FSCIL)\n- Event Camera Object Detection\n- Non-human Primate (NHP) Motor Prediction\n- Chaotic Function Prediction\n\nAdditional benchmarks\n~~~~~~~~~~~~~~~~~~~~~\n- DVS Gesture Recognition\n- Google Speech Commands (GSC) Classification\n- Neuromorphic Human Activity Recognition (HAR)\n\nGetting started\n---------------\n\nExample benchmark scripts can be found under the ``neurobench/examples`` folder. \n(`https://github.com/NeuroBench/neurobench/tree/main/neurobench/examples/ <https://github.com/NeuroBench/neurobench/tree/main/neurobench/examples/>`__)\n\nIn general, the design flow for using the framework is as follows:\n\n1. Train a network using the train split from a particular dataset.\n2. Wrap the network in a ``NeuroBenchModel``.\n3. Pass the model, evaluation split dataloader, pre-/post-processors,\n   and a list of metrics to the ``Benchmark`` and ``run()``.\n\nDocumentation for the framework interfaces can found in the `API Overview <https://neurobench.readthedocs.io/en/latest/api.html>`__.\n\nDevelopment\n-----------\n\nIf you clone the repo directly for development, `poetry <https://pypi.org/project/poetry/>`__ \ncan be used to maintain a virtualenv consistent with a deployment environment. In the\nroot directory run:\n\n::\n\n   pip install poetry\n   poetry install\n\nPoetry requires python >=3.9. Installation should not take more than a few minutes.\n\nEnd-to-end examples can be run from the poetry environment. As a demo, try the \nGoogle Speech Commands keyword classification benchmark:\n\n::\n\n   # ANN Benchmark Example\n   poetry run python neurobench/examples/gsc/benchmark_ann.py\n   \n   # Expected results:\n   # {'footprint': 109228, 'connection_sparsity': 0.0,\n   # 'classification_accuracy': 0.8653339397251905, 'activation_sparsity': 0.3854464619019532, \n   # 'synaptic_operations': {'Effective_MACs': 1749994.1556565198, 'Effective_ACs': 0.0, 'Dense': 1902179.0}}\n\n\n   # SNN Benchmark Example\n   poetry run python neurobench/examples/gsc/benchmark_snn.py\n   \n   # Expected results:\n   # {'footprint': 583900, 'connection_sparsity': 0.0,\n   # 'classification_accuracy': 0.8484325295196562, 'activation_sparsity': 0.9675956131759854, \n   # 'synaptic_operations': {'Effective_MACs': 0.0, 'Effective_ACs': 3556689.9895502045, 'Dense': 29336955.0}}\n\nThese demos should download the dataset, then run in a couple minutes. Other baseline result scripts and notebook\ntutorials are available in the ``neurobench/examples`` folder.\n\nDevelopers\n----------\n\nNeuroBench is a collaboration between industry and academic engineers\nand researchers. This framework is currently maintained by `Jason\nYik <https://www.linkedin.com/in/jasonlyik/>`__, `Noah\nPacik-Nelson <https://www.linkedin.com/in/noah-pacik-nelson/>`__, and\n`Korneel Van den\nBerghe <https://www.linkedin.com/in/korneel-van-den-berghe/>`__, and\nthere have been technical contributions from many others. A\nnon-exhaustive list includes Gregor Lenz, Denis Kleyko, Younes\nBouhadjar, Paul Hueber, Vincent Sun, Biyan Zhou, George Vathakkattil\nJoseph, Douwe den Blanken, Maxime Fabre, Shenqi Wang, Guangzhi Tang,\nAnurag Kumar Mishra, Soikat Hasan Ahmed, Benedetto Leto, Aurora Micheli,\nTao Sun.\n\nContributing\n------------\n\nIf you are interested in helping to build this framework, please see the\n`Contribution Guidelines <https://neurobench.readthedocs.io/en/latest/contributing.html>`__.\n\nCitation\n--------\n\nIf you use this framework in your research, please cite the following\npreprint article:\n\n::\n\n   @misc{yik2024neurobench,\n      title={NeuroBench: A Framework for Benchmarking Neuromorphic Computing Algorithms and Systems}, \n      author={Jason Yik and Korneel Van den Berghe and Douwe den Blanken and Younes Bouhadjar and Maxime Fabre and Paul Hueber and Denis Kleyko and Noah Pacik-Nelson and Pao-Sheng Vincent Sun and Guangzhi Tang and Shenqi Wang and Biyan Zhou and Soikat Hasan Ahmed and George Vathakkattil Joseph and Benedetto Leto and Aurora Micheli and Anurag Kumar Mishra and Gregor Lenz and Tao Sun and Zergham Ahmed and Mahmoud Akl and Brian Anderson and Andreas G. Andreou and Chiara Bartolozzi and Arindam Basu and Petrut Bogdan and Sander Bohte and Sonia Buckley and Gert Cauwenberghs and Elisabetta Chicca and Federico Corradi and Guido de Croon and Andreea Danielescu and Anurag Daram and Mike Davies and Yigit Demirag and Jason Eshraghian and Tobias Fischer and Jeremy Forest and Vittorio Fra and Steve Furber and P. Michael Furlong and William Gilpin and Aditya Gilra and Hector A. Gonzalez and Giacomo Indiveri and Siddharth Joshi and Vedant Karia and Lyes Khacef and James C. Knight and Laura Kriener and Rajkumar Kubendran and Dhireesha Kudithipudi and Yao-Hong Liu and Shih-Chii Liu and Haoyuan Ma and Rajit Manohar and Josep Maria Margarit-Taulé and Christian Mayr and Konstantinos Michmizos and Dylan Muir and Emre Neftci and Thomas Nowotny and Fabrizio Ottati and Ayca Ozcelikkale and Priyadarshini Panda and Jongkil Park and Melika Payvand and Christian Pehle and Mihai A. Petrovici and Alessandro Pierro and Christoph Posch and Alpha Renner and Yulia Sandamirskaya and Clemens JS Schaefer and André van Schaik and Johannes Schemmel and Samuel Schmidgall and Catherine Schuman and Jae-sun Seo and Sadique Sheik and Sumit Bam Shrestha and Manolis Sifalakis and Amos Sironi and Matthew Stewart and Kenneth Stewart and Terrence C. Stewart and Philipp Stratmann and Jonathan Timcheck and Nergis Tömen and Gianvito Urgese and Marian Verhelst and Craig M. Vineyard and Bernhard Vogginger and Amirreza Yousefzadeh and Fatima Tuz Zohora and Charlotte Frenkel and Vijay Janapa Reddi},\n      year={2024},\n      eprint={2304.04640},\n      archivePrefix={arXiv},\n      primaryClass={cs.AI}\n   }\n",
    'author': 'NeuroBench Team',
    'author_email': 'neurobench@googlegroups.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
