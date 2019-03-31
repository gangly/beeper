#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
autotesttask.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/11/9 14:50
"""
from beeper.lib import prestodb
from beeper.lib.mysqldb import MySQL
from beeper.task import Task


class AutotestTask(Task):
    _tasktype = 'autotest'

    def parse_conf(self, conf):

        lines = conf.split("\n")
        conf_lines = [line for line in lines if line.startswith('#')]
        assert len(conf_lines) == 2, "没找到测试主题或邮件发送人列表"

        subject = conf_lines[0].replace('#', '')
        receivers_names = conf_lines[1].replace('#', '').replace(' ', '').split(',')
        receivers = self.add_email_suffix(receivers_names)

        filtered_lines = [line.replace("\n", ' ').replace('"', '').strip() for line in lines if
                          not line.startswith('--') and not line.startswith('#')]
        content = ' '.join(filtered_lines)
        split_sqls = content.split(';')
        sqls = [sql for sql in split_sqls if sql]
        assert len(sqls) % 2 == 0, "测试的sql数不为偶数"

        base_sqls = []

        i = 0
        while i < len(sqls):
            base_sqls.append({'base': sqls[i], 'test': sqls[i + 1]})
            i += 2
        return {
            'subject': subject,
            'receivers': receivers,
            'sqls': base_sqls
        }

    def make_table(self, conf):
        tables = []
        rows = self.get_data(conf['sqls'])
        headers = ['测试sql', '查询结果', '测试差值', '是否通过测试']
        tables.append({'desc': conf['subject'], 'headers': headers, 'rows': rows})
        return {'head': conf['subject'], 'tables': tables}

    def check_value(self, val1, val2):
        res = False
        if val1 is None or val2 is None:
            res = False
        elif round(val1, 2) != round(val2, 2):
            res = True
        return res

    def get_data(self, sqls):

        db = prestodb.Presto()
        # db = MySQL('local')

        rows = []
        for sql in sqls:

            basesql = self.clean_sql(sql['base'])
            print(basesql)
            res = db.query_fetchall(basesql)
            base = res[0][0] if len(res) > 0 else 0.0

            testsql = self.clean_sql(sql['test'])
            print(testsql)
            res = db.query_fetchall(testsql)
            test = res[0][0] if len(res) > 0 else 0.0
            warn = self.check_value(base, test)

            passed = 'Yes' if not warn else 'No'
            items = [
                [self.back_sql(basesql), self.back_sql(testsql)],
                '%s/%s' % (base, test),
                self.toint(test) - self.toint(base),
                passed
            ]

            rows.append({'warn': warn, 'items': items})
        return rows

    def clean_sql(self, sql):
        sql = sql
        return sql.replace('%', '%%').replace("\u2028", '').replace("\u2029", '')

    def back_sql(self, sql):
        return sql.replace('%%', '%')

    def toint(self, val):
        return int(val) if val is not None else 0