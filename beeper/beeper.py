#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
beeper.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/11/9 15:52
"""
import sys

from checkdatatask import CheckdataTask
from autotesttask import AutotestTask

if __name__ == '__main__':

    args = sys.argv[1:]
    # args = ['autotest',]
    if len(args) < 1:
        print """Usage:python beeper.py tasktype
                    tasktype: checkdata autotest
            """
        exit(1)

    (tasktype, ) = args
    task = eval(tasktype.capitalize()+'Task')()
    task.execute_task()

