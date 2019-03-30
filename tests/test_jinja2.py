#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
test_jinja2.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/10/27 16:01
"""

from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('lib', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    keep_trailing_newline=True,
)


def test_for():
    template = env.get_template('auto_test_temp.html')
    headers = ['col1', 'col2']
    rows = [
        {'warn': False, 'items': [["sdfsdwer", 'sdf'], '2134d']},
        {'warn': True, 'items': [['3werd', '234'], 'erwtwer']}
    ]

    tables = [
        {'desc': 'table1', 'headers': headers, 'rows': rows},
        {'desc': 'table2', 'headers': headers, 'rows': rows},
    ]
    content = template.render(head='a test', tables=tables)
    print content
