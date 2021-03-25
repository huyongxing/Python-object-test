#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/15 16:46
# @Author   : huyx
# @Site     : 
# @File     : time_function_test.py
# @Software : PyCharm

import time

# # 获取当前时间戳
# ticks = time.time()
# print("当前时间戳为：", ticks)
#
# # 获取当前时间
# localtime = time.localtime(time.time())
# print("本地时间为：", localtime)
#
# # 获取格式化的时间
# localtime = time.asctime(time.localtime(time.time()))
# print("本地时间为：", localtime)
#
# # 格式化日期 time.strftime(format[, t])
# # 格式化成 XXXX-XX-XX XX:XX:XX 形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#
# # 格式化成Sat Mar 28 22:24:23 2016形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# print(time.strftime("%A %B %d %H:%M:%S %Y", time.localtime()))
#
# # 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:23 2016"
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
#
# # 获取某月日历
# import calendar
#
# cal = calendar.month(2016, 1)
# print("以下输出2021年3月份的日历：")
# print(cal)
#
# # calendar.isleap(year) 闰年返回True，平年返回False
# print(calendar.isleap(2021))
# print(calendar.isleap(2020))

from datetime import date
today = date.today()
print(today)

print(today == date.fromtimestamp(time.time()))

my_birthday = date(today.year, 6, 25)
if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)

time_to_birthday = abs(my_birthday - today)
print(time_to_birthday.days)