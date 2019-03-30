#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
utils.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/9/11 11:30
"""
import usetime


def check_key(dct, path):

    if_error = False
    val = dct
    try:
        if path.contains('.'):
            keys = path.split('.')
            for key in keys:
                val = val[key]
        else:
            val = val[path]
    except KeyError as e:
        print '配置文件必须包含%s字段' % (path.split('.')[-1])
        if_error = True
    return if_error

frmat = "%Y-%m-%d"
datemark = {
        '$lastweekday': usetime.getlastweekday(frmat),
        '$lastweekyesday': usetime.getlastweekyesday(frmat),
        '$yesterday': usetime.getyesterday(frmat),
        '$today': usetime.gettoday(frmat),
        '$beforeyesday': usetime.getbeforeyesterday(frmat),
        '$day_today': usetime.getday_today(),
        '$day_yesterday': usetime.getday_yesterday(),
        '$day_lastweekday': usetime.getday_lastweekday(),
        '$day_lastweekyesday': usetime.getday_lastweekyesday(),
        '$day_beforeyesday': usetime.getday_beforeyesday()
    }


def replace_date_mark(text):
    """
     替换日期标记
     :param text: 字符串 
     :return: 替换后的字符串
     """
    for key, value in datemark.items():
        text = text.replace(key, value)
    return text
