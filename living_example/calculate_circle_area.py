#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/16 14:12
# @Author   : huyx
# @Site     : 
# @File     : calculate_circle_area.py
# @Software : PyCharm

def findArea(r):
    PI = 3.142
    return PI * (r * r)

# 调用方法
print("圆的面积为：%.6f" % findArea(5))
