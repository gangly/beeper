#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
test.py.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/9/8 09:39
"""
from beeper.autotest import clean_sql
from beeper.lib.prestodb import Presto
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


"""
本地测试
"""


def test_singleton():
    db1 = Presto('prepub')
    db2 = Presto('prepub')

    print db1
    print db2
    assert db1 == db2


def test_presto():
    print 'start test presto'
    db = Presto('prepub')
    print db
    # sql = "SELECT sum(uv) from hive.bdc_dm.res_flowcloud_topology_categorytocategory limit 10 "
    sql = "SELECT sum(uv) from hive.bdc_dm.res_flowcloud_topology_category_total where landing_date = '2017-10-29' and channel1 = '自然搜索' and url_category = '首页' and ORDER_rule=1 and url_category_group=2"

    print sql
    results = db.query_fetchall(clean_sql(sql))
    print results




