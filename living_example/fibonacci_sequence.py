#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/18 14:05
# @Author   : huyx
# @Site     : 
# @File     : fibonacci_sequence.py
# @Software : PyCharm

nterms = int(input("你需要几项？"))

n1 = 0
n2 = 1
count = 2

if nterms <= 0:
    print("请输入一个正整数")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=",")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=",")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1
