#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
beeper.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/11/7 15:03
"""
import os
from abc import abstractmethod

from beeper.lib.emailsender import EmailSender

from beeper.constant import EMAIL_SUFFIX


class Task(object):
    """报警器"""

    _tasktype = 'task'

    def get_template(self):
        from jinja2 import Environment, PackageLoader, select_autoescape
        env = Environment(
            loader=PackageLoader('lib', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        return env.get_template(self._tasktype + '.html')

    def read_conf(self):
        jobconfsdir = os.path.join(os.getcwd(), 'beeper', 'taskconfs', self._tasktype)
        # jobconfsdir = os.path.join(os.getcwd(), 'confs', self._tasktype)
        print('jobconfsdir: %s' % jobconfsdir)
        confs = []
        for filename in os.listdir(jobconfsdir):
            if not filename.endswith('.conf'):
                continue
            filepath = os.path.join(jobconfsdir, filename)
            print('reading file: %s ' % filepath)
            with open(filepath) as fp:
                conf = fp.read()
                confs.append(self.parse_conf(conf))
        return confs

    @abstractmethod
    def parse_conf(self, conf):
       pass

    @abstractmethod
    def make_table(self, conf):
        pass

    def add_email_suffix(self, elist, suffix=EMAIL_SUFFIX):
        return [receiver+suffix for receiver in elist] if suffix else elist

    def send_emails(self, emails):
        emailsender = EmailSender()
        for email in emails:
            print(email)
            emailsender.send(email)

    def execute_task(self):
        # import sys
        # reload(sys)
        # sys.setdefaultencoding("utf-8")

        emails = []
        template = self.get_template()
        confs = self.read_conf()
        for conf in confs:
            data = self.make_table(conf)
            if data:
                content = template.render(data=data)
                email = {
                    'receivers': conf['receivers'],
                    'subject': conf['subject'],
                    'content': content
                }
                emails.append(email)
        if emails:
            print('正在发送邮件....')
        self.send_emails(emails)


