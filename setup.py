#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
setup.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/11/10 17:54
"""

#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

'''
把redis服务打包成C:\Python27\Scripts下的exe文件
'''

setup(
    name="beeper",  #pypi中的名称，pip或者easy_install安装时使用的名称，或生成egg文件的名称
    version="1.0",
    author="Gary Li",
    author_email="gangly123@163.com",
    description=("This is a simple data checking tool"),
    license="GPLv3",
    keywords="data check",
    url="http://pypi.python.org/pypi/beeper/",
    packages=['beeper'],  # 需要打包的目录列表

    # 需要安装的依赖
    install_requires=[
        'setuptools>=16.0',
        'SQLAlchemy>=1.1.9'
    ],

    # 添加这个选项，在windows下Python目录的scripts下生成exe文件
    # 注意：模块与函数之间是冒号:
    entry_points={'console_scripts': [
        'redis_run = beeper.beeper:main',
    ]},

    # long_description=read('README.md'),
    classifiers=[  # 程序的所属分类列表
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    # 此项需要，否则卸载时报windows error
    zip_safe=False
)