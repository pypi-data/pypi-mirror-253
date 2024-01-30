# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qwen']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch', 'zetascale']

setup_kwargs = {
    'name': 'qwen',
    'version': '0.1.1',
    'description': 'Qwen VL - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n\n# Qwen-VL\nMy personal implementation of the model from "Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities", they haven\'t released model code yet sooo... \nFor more details, please refer to the\xa0[full paper](https://doi.org/10.48550/arXiv.2308.12966).\n\n\n# Install\n`pip3 install qwen`\n\n---\n\n# Usage\n```python\n\n# Importing the necessary libraries\nimport torch\nfrom qwen import Qwen\n\n# Creating an instance of the Qwen model\nmodel = Qwen()\n\n# Generating random text and image tensors\ntext = torch.randint(0, 20000, (1, 1024))\nimg = torch.randn(1, 3, 256, 256)\n\n# Passing the image and text tensors through the model\nout = model(img, text)  # (1, 1024, 20000)\n\n```\n\n# Todo\n\n- [ ] Position aware vision language adapter, compresses image features. Singer layer cross attention module inited randomly => group of trainable embeddings as query vectors + image features from the visual encoder as keys for cross attention ops => OUTPUT: compresses visual feature sequence to a fixed lnegth of 256, 2d absolute positional encodings are integrated into the cross attentions mechanisms query key pairs => compressed feature sequence of length of 256 => fed into decoder llm\n\n- [ ] Bounding Boxes, for any given accurate bounding box, a norm process is applied in the range [0, 1000] and transformed into a string format (Xtope, Ytople)(Xottomright, Ybottomright) -> the string is tokenized as text and does not require positional vocabulary. Detection strings and regular text strings, two special tokens <box> and </box> are added to the beginning and end of the bounding box string. + another sed of special tokens (<ref> and </ref>) is introduced.\n\n# Citations\n\nPlease use the following to cite this work:\n\n```bibtex\n@article{bai2023qwen,\n  title={Qwen-VL: A Frontier Large Vision-Language Model with Versatile Abilities},\n  author={Bai, Jinze and Bai, Shuai and Yang, Shusheng and Wang, Shijie and Tan, Sinan and Wang, Peng and Lin, Junyang and Zhou, Chang and Zhou, Jingren},\n  journal={arXiv preprint arXiv:2308.12966},\n  year={2023},\n  url={https://doi.org/10.48550/arXiv.2308.12966}\n}\n\n```',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/Qwen-VL',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
