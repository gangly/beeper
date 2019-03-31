#!/usr/bin/env python 2.7
# -*- coding: UTF-8 -*-
"""
Project: 
checkdatatask.py

@authors: Gary Li
@contact: gangly123@163.com
@site: http://my.csdn.net/freefishly
@version: python2.7
@create time: 2017/11/9 13:55
"""
import subprocess
import traceback

from beeper.lib import mysqldb, prestodb
from beeper.lib.utils import replace_date_mark
from beeper.task import Task


class CheckdataTask(Task):

    _tasktype = 'checkdata'

    def parse_conf(self, conf):
        content = eval(replace_date_mark(conf))
        content['subject'] = content['title']
        content['receivers'] = self.add_email_suffix(content['receivers'])
        return content

    def make_table(self, conf):
        tables = []
        for jobconf in conf['jobs']:
            sql = jobconf['sql']
            headers = jobconf['headers']
            data = self.get_data(jobconf['source'], sql, headers)
            if_warn, checked_data = self.check_warn(data, headers, jobconf['check'])

            percent = jobconf['percent'] if 'percent' in jobconf else []
            rows = self.make_percent(checked_data, percent, headers)
            table = {'desc': jobconf['desc'], 'headers': headers, 'rows': rows}
            if if_warn:
                tables.append(table)
        return {'head': conf['head'], 'tables': tables} if tables else False

    def get_data(self, source, sql, headers):
        """
        查询获取数据，并整理
        :param sql: 查询语句
        :param headers: 表头
        :return: 整理好数据集
        """
        data = []
        if source.startswith('mysql'):
            dbmark = source.split(':')[-1]
            data = self.query_mysql(dbmark, sql, headers)
        elif source == 'presto':
            data = self.query_presto(sql, headers)
        elif source == 'hive':
            data = self.query_hive(sql, headers)
        else:
            print('wrong database source')
            exit(1)
        return data

    def arrange_datasets(self, datasets, headers):
        data = []
        for row in datasets:
            row = list(row)
            item = {}
            for index, header in enumerate(headers):
                item[header] = row[index]
            data.append(item)
        return data

    def query_mysql(self, dbmark, sql, headers):

        db = mysqldb.MySQL(dbmark)
        results = db.query_fetchall(sql)

        return self.arrange_datasets(results, headers)

    def query_presto(self, sql, headers):
        db = prestodb.Presto()
        results = db.query_fetchall(sql)
        return self.arrange_datasets(results, headers)

    def query_hive(self, sql, headers):

        cmd = '''hive -e "%s" ''' % (sql,)
        print(cmd)
        data = []

        try:
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            while True:
                line = p.stdout.readline()
                if line == '' and p.poll() is not None:
                    break

                words = line.split("\t")
                print(len(words))
                if len(words) < len(headers):
                    continue
                item = {}
                for index, header in enumerate(headers):
                    item[header] = words[index].strip()

                data.append(item)
                print(line)
        except Exception as re:
            print("message is:%s" % (str(re)))
            traceback.print_exc()
        return data

    def check_warn(self, data, headers, check):
        """
        检查数据质量
        :param data:数据集 
        :param headers: 表头
        :param check: 检查表达式
        :return: 标记后的数据集
        """
        if_warn = False
        if_none = False
        res = []
        for item in data:
            expression = check

            for header in headers:
                print(expression)
                if item[header] is None:
                    if_none = True
                expression = expression.replace(header, 'abs(%s)' % str(item[header]))

            # 如果有none数据，则跳过这次检测
            if if_none:
                if_none = False
                continue

            print('check expression: %s ' % expression)
            rows = {'data': item}
            if eval(expression):
                if_warn = True
                rows['warn'] = True
            else:
                rows['warn'] = False
            res.append(rows)
        return if_warn, res

    def make_percent(self, data, percent, headers):
        rows = []
        for item in data:
            # 处理百分号字段
            for header in percent:
                item['data'][header] = str(round(100 * float(item['data'][header]), 2)) + '%'
            items = [str(item['data'][header]) for header in headers]
            row = {'warn': item['warn'], 'items': items}
            rows.append(row)
        return rows