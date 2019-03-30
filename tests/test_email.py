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
from beeper.lib.emailsender import EmailSender


def test_email():
    receivers = ['gangly123@163.com']
    email = EmailSender(receivers)
    email.send('ttt', 'hah', 'test')