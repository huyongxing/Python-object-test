#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/16 17:10
# @Author   : huyx
# @Site     : 
# @File     : celsius_to_fahrenheit.py
# @Software : PyCharm

# # 接收用户输入
# celsius = float(input('输入摄氏温度：'))
#
# # 计算华氏温度
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f 摄氏温度转为华氏温度为：%0.1f ' % (celsius, fahrenheit))


fahrenheit = float(input('输入华氏温度：'))

# 计算摄氏温度
celsius = (fahrenheit - 32) / 1.8
print('%0.1f 华氏温度转为摄氏温度为：%0.1f' % (fahrenheit, celsius))