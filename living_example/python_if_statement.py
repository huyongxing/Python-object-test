#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/17 9:12
# @Author   : huyx
# @Site     :
# @File     : python_if_statement.py
# @Software : PyCharm

# # 使用 if...elif...elif 语句判断数字
# num = float(input("输入一个数字："))
#
# if num > 0:
#     print("正数")
# elif num == 0:
#     print("零")
# else:
#     print("负数")

# # 使用内嵌 if 语句
# num = float(input("输入一个数字："))
#
# if num >= 0:
#     if num == 0:
#         print("零")
#     else:
#         print("正数")
# else:
#     print("负数")

while True:
    try:
        num = float(input('请输入一个数字：'))
        if num == 0:
            print('输入的数字是零')
        elif num > 0:
            print('输入的数字是正数')
        else:
            print('输入的数字是负数')
        break
    except ValueError:
        print('输入无效，请输入一个数字！')