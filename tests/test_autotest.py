#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
test_email.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/10/25 17:27
"""
import os

from beeper.autotest import parse_conf, clean_sql


def test_clean_sql():
    assert clean_sql("select * from tb where aa like 't%'") == "select * from tb where aa like 't%%'"


def test_paser_conf():
    filepath = os.path.join(os.getcwd(), 'beeper','autotests', 'flowcloud.conf')
    sqls = parse_conf(filepath)
    for sql in sqls:
        print 'base: ', sql['base']
        print 'test: ', sql['test']