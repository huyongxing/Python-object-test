#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/15 11:18
# @Author   : huyx
# @Site     : 
# @File     : update_mysql_table.py
# @Software : PyCharm

import pymysql

db = pymysql.connect(host="172.16.8.111", user="huyx", passwd="123456", database="yichedb-huyx")

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
