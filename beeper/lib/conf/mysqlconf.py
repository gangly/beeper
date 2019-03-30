#!/usr/bin/env python 2.7
# -*- coding:utf-8 -*-
'''
     * 数据库库名与集群编号的映射关系表，说明每个数据库部署在哪个集群上
     * 每增加一个数据库时必须在这里增加一个映射记录，如果不增加映射记录，
     * 则默认认为该数据库部署在第一个集群上
     * @var array
'''


DB_NAMES = {
    # 本地xampp测试库
    'local_test': {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'root',
        'db': 'test',
        'charset': 'utf8'
    },
    'local': {
        'host': 'localhost',
        'port': 3306,
        'db': 'test',
        'user': 'root',
        'passwd': 'root',
        'charset': 'utf8'
    },
}


# 连接重试次数及间隔时间
TRY_LINK_COUNT = 2
INTERVAL_TIME_SECOND = 5
