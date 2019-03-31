#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
prestodb.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/9/12 16:28
"""


from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from beeper.lib.metasingleton import MetaSingleton
from beeper.lib.conf import prestoconf


class Presto(object):
    __metaclass__ = MetaSingleton

    _session = None

    def __init__(self, dbname='online'):
        if self._session is None:
            if dbname not in prestoconf.presto_con:
                raise Exception('presto dbname is wrong!')
            engine = create_engine(prestoconf.presto_con[dbname])
            db_session = sessionmaker(bind=engine)
            self._session = db_session()

    def query_fetchall(self, sql):
        return self._session.execute(sql).fetchall()
