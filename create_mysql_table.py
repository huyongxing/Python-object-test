#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/15 10:39
# @Author   : huyx
# @Site     : 
# @File     : create_mysql_table.py
# @Software : PyCharm

import pymysql

# 创建数据库连接
db = pymysql.connect(host="172.16.8.111", user="huyx", passwd="123456", database="yichedb-huyx")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE(
            FIRST_NAME CHAR(20) NOT NULL,
            LAST_NAME CHAR(20),
            AGE INT,
            SEX CHAR(1),
            INCOME FLOAT)"""

# 关闭数据库连接
cursor.execute(sql)

db.close()