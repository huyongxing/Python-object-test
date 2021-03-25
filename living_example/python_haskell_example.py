#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/18 13:32
# @Author   : huyx
# @Site     : 
# @File     : python_haskell_example.py
# @Software : PyCharm

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{}*{}={}\t'.format(j, i, i * j), end='')
    print()
