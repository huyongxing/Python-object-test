#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/16 17:27
# @Author   : huyx
# @Site     : 
# @File     : switching_variable.py
# @Software : PyCharm

x = input('输入 x 的值：')
y = input('输入 y 的值：')

# # 创建临时变量，并交换
# temp = x
# x = y
# y = temp

# 不使用临时变量
x, y = y, x

print('交换后 x 的值为：{}'.format(x))
print('交换后 y 的值为：{}'.format(y))
