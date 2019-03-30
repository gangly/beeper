#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
###############################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
###############################################################################
"""
read email.list and send email

Authors: Gary(ligang05@baidu.com)
Date:    2015/07/07 17:23:06
"""


import smtplib
from email.mime.text import MIMEText

from metasingleton import MetaSingleton
from conf.emailconf import sender, host, user, password


class EmailSender(object):
    """邮件发送类"""
    __metaclass__ = MetaSingleton
    _smtp = None

    def __init__(self):
        if self._smtp is None:
            self._smtp = smtplib.SMTP()
            self._smtp.connect(host)
            self._smtp.login(user, password)
            self._smtp.ehlo()

    def __del__(self):
        if self._smtp:
            self._smtp.close()

    def send(self, email):
        """发送邮件"""
        receivers = email['receivers']
        subject = email['subject']
        content = email['content']

        if not receivers:
            print "There are no receivers,please check email.list"
            exit(1)

        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ", ".join(receivers)
        try:
            print 'email send to ', receivers
            self._smtp.sendmail(sender, receivers, msg.as_string())
        except Exception as e:
            print "Send email error: %s" % e
