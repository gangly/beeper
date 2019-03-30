#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
###############################################################################
#
# Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
#
###############################################################################
"""
封装的有关时间操作的函数

Authors: Gary(ligang05@baidu.com)
Date:    2015/07/07 17:23:06
"""

import datetime


def gettoday(frmat='%Y%m%d'):
    """
    获取当天的日期
    frmat为返回字符串格式
    """
    return datetime.date.today().strftime(frmat)


def getday_before_after_today(days, frmat='%Y%m%d'):
    """
    获取与当天相差days天数的日期
    days: 相隔的天数，-2=>两天前，+4=>4天后
    """
    day = datetime.date.today() + datetime.timedelta(days=days)
    return day.strftime(frmat)


def getyesterday(frmat='%Y%m%d'):
    """
    获取昨天的日期
    frmat为返回字符串格式
    """
    return getday_before_after_today(-1, frmat)

def getbeforeyesterday(frmat='%Y%m%d'):
    """
    获取前天的日期
    frmat为返回字符串格式
    """
    return getday_before_after_today(-2, frmat)


def getlastweekday(frmat='%Y%m%d'):
    "获取今日上周同日"
    return getday_before_after_today(-7, frmat)


def getlastweekyesday(frmat='%Y%m%d'):
    "获取昨日上周同日"
    return getday_before_after_today(-8, frmat)




def gettomorrow(frmat='%Y%m%d'):
    """
    获取明天的日期
    frmat为返回字符串格式
    """
    return getday_before_after_today(1, frmat)


# ##########获取天01-31########################


def getdayfromdate(dt):
    return dt[-2:]


def getday_today():
    return getdayfromdate(gettoday())


def getday_yesterday():
    return getdayfromdate(getyesterday())


def getday_lastweekday():
    return getdayfromdate(getlastweekday())


def getday_lastweekyesday():
    return getdayfromdate(getlastweekyesday())


def getday_beforeyesday():
    return getdayfromdate(getbeforeyesterday())

# ##############获取小时#####################


def getnowhour(frmat='%Y%m%d%H'):
    """
    获取小时 2015082001-2015082023
    """
    return datetime.datetime.now().strftime(frmat)


def gethour_before_after_now(hours, frmat='%Y%m%d%H'):
    """
    获取与当前小时相差hours小时的日期
    days: 相隔的小时数，-2=>两小时前，+4=>4小时后
    """
    hour = datetime.datetime.now() + datetime.timedelta(hours=hours)
    return hour.strftime(frmat)


def getlasthour(frmat='%Y%m%d%H'):
    """
    获取上一个小时
    """
    return gethour_before_after_now(-1, frmat)

