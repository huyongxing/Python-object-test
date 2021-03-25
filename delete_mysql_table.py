#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/15 11:33
# @Author   : huyx
# @Site     : 
# @File     : delete_mysql_table.py
# @Software : PyCharm

import pymysql

db = pymysql.connect(host="172.16.8.111", user="huyx", passwd="123456", database="yichedb-huyx")

cursor = db.cursor()

sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()