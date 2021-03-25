#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/15 10:53
# @Author   : huyx
# @Site     : 
# @File     : insert_mysql_table.py
# @Software : PyCharm

import pymysql

# 创建数据库连接
db = pymysql.connect(host="172.16.8.111", user="huyx", passwd="123456", database="yichedb-huyx")

# 使用 cursor() 方法获取操作游标
cursor = db.cursor()

# SQL插入语句
sql = """INSERT INTO EMPLOYEE (FIRST_NAME,
            LAST_NAME, AGE, SEX, INCOME)
            VALUES ('Mac', 'Mohan', '20', 'M', '2000')"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()