#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/16 13:11
# @Author   : huyx
# @Site     : 
# @File     : python_square_root.py
# @Software : PyCharm

# # 通过指数运算符 ** 来计算平方根,只适用于正数
# num = float(input('请输入一个数字：'))
# num_sqrt = num ** 0.5
# print('%0.3f 的平方根为 %0.3f' % (num, num_sqrt))

# 负数和复数的平方根计算
import cmath

num = int(input("请输入一个数字："))
num_sqrt = cmath.sqrt(num)
print('{0}的平方根为：{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
