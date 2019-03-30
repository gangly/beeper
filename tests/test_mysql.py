#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
test_mysql.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/10/25 17:24
"""
from beeper.lib.mysqldb import MySQL


def test_singleton():
    db1 = MySQL('local')
    db2 = MySQL('local')
    print db1
    print db2


def test_mysql():
    '''使用样例'''
    # 连接数据库，创建这个类的实例
    # db = MySQL('local_test')
    db = MySQL('local')
    print db

    #操作数据库
    sql = "SELECT * FROM stu "
    db.query(sql)

    #获取结果列表
    result = db.query_fetchall(sql)
    # result = db.query_onerow(sql)
    print result

    print db.show_tables()

    # data = {
    #     'subject': 'werewr',
    #     'reply_to': 5,
    #     'text': 'nedw-text',
    # }
    # # db.insert('messages', data)
    # #
    #
    # newdata = {}
    # for key, val in data.items():
    #     if isinstance(val, unicode):
    #         newdata[key] = val.encode('utf8')
    # db = MySQL('light_statistics')
    # db.insert_update('house_base_info', newdata)
    # db.commit()
