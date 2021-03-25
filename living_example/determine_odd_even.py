#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/17 11:10
# @Author   : huyx
# @Site     : 
# @File     : determine_odd_even.py
# @Software : PyCharm

# Python 判断奇数偶数
# 如果是偶数除以 2 余数为 0
# 如果余数为 1 则为奇数

# num = int(input('输入一个数字：'))
# if (num % 2) == 0:
#     print("{0} 是偶数".format(num))
# else:
#     print("{0} 是奇数".format(num))

# 添加错误提示
while True:
    try:
        num = int(input('输入一个数字：'))
        if (num % 2) == 0:
            print("{0}是偶数".format(num))
        else:
            print("{0}是奇数".format(num))
        break
    except ValueError:
        print("无效输入，请输入数字！")