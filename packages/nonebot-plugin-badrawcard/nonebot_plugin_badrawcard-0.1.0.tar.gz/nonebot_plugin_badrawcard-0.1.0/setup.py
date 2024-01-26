# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_badrawcard']

package_data = \
{'': ['*'], 'nonebot_plugin_badrawcard': ['Data/*', 'Data/student_icons/*']}

install_requires = \
['aiofiles>=23.2.1,<24.0.0',
 'httpx>=0.25.0,<0.26.0',
 'loguru>=0.7.2,<0.8.0',
 'nonebot-adapter-onebot>=2.3.1,<3.0.0',
 'nonebot2>=2.1.3,<3.0.0',
 'pillow>=10.0.1,<11.0.0',
 'pydantic[dotenv]>=1.10.0,<2.0.0',
 'redis>=5.0.0,<6.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-badrawcard',
    'version': '0.1.0',
    'description': '模拟BA抽卡',
    'long_description': '# Test',
    'author': 'LMZZ',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/lengmianzz/nonebot-plugin-BAdrawcard',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
