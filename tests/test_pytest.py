#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
test_pytest.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/10/23 14:34
"""
import pytest


def func(x):
    return x + 1


def test_func():
    assert func(4) == 5


def test_str():
    assert 'tdd' == 'tdd'
