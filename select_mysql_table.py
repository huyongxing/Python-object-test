#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/15 11:03
# @Author   : huyx
# @Site     : 
# @File     : select_mysql_table.py
# @Software : PyCharm

import pymysql

db = pymysql.connect(host="172.16.8.111", user="huyx", passwd="123456", database="yichedb-huyx")

cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE \
        WHERE INCOME > %s" % (1000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

db.close()
