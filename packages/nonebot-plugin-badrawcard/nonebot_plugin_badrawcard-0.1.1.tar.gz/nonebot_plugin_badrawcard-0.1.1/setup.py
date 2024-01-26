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
    'version': '0.1.1',
    'description': '模拟BA抽卡',
    'long_description': '<div align="center">\n\n# 《碧蓝档案》抽卡模拟器 \n\n</div>\n\n<p align="center">\n  <img src="https://img.shields.io/github/license/lengmianzz/nonebot-plugin-BAdrawcard" alt="license">\n  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">\n  <img src="https://img.shields.io/badge/nonebot-2.0.0+-red.svg" alt="NoneBot">\n</p>\n\n## **Warning**: 本插件需要安装Redis!!!  \n\n### 功能:\n - 跟随游戏概率进行模拟抽卡\n - 自动更新up卡池\n - 长时间未用, 自动更新卡池\n - 展示当前UP学生\n - 展示当前概率\n\n\n### 安装:\n - 使用 nb-cli 安装  \n```\nnb plugin install nonebot-plugin-BAdrawcard\n```\n\n\n### 配置:\n - proxy: 代理, `http://ip:host`格式\n - redis_host: Redis的host, 默认为localhost\n - redis_port: Redis的开放端口, 默认为6379   \n\n\n### 触发:\n - `/ba单抽`\n - `/ba十连`\n - `/ba来一井`\n - `/当前概率`\n - `/当前up`\n',
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
