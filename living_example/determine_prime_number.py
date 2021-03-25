#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/17 12:31
# @Author   : huyx
# @Site     : 
# @File     : determine_prime_number.py
# @Software : PyCharm

# Python 程序用于检测用户输入的数字是否为质数

# 用户输入数字
num = int(input("请输入一个数字："))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘以", num // i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")
