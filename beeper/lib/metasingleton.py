#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
metasingleton.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/11/10 09:39
"""


class MetaSingleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.instance

    def __new__(cls, name, bases, dct):
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(MetaSingleton, cls).__init__(name, bases, dct)

