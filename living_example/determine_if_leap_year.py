#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/17 11:36
# @Author   : huyx
# @Site     : 
# @File     : determine_if_year.py
# @Software : PyCharm

year = int(input("输入一个年份："))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0}是闰年".format(year))
        else:
            print("{0}不是闰年".format(year))
    else:
        print("{0}是闰年".format(year))
else:
    print("{0}不是闰年".format(year))
