#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/17 12:50
# @Author   : huyx
# @Site     : 
# @File     : outputs_specified_range_prime.py
# @Software : PyCharm

# take input from the user
# lower = int(input("输入区间最小值："))
# upper = int(input("输入区间最大值："))
#
# for num in range(lower, upper + 1):
#     # 素数大于 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

# 使用 Numpy 提高速度
from datetime import date
import time
import numpy as np
#
today = date.today()
#
lower = int(input("Starting Number:"))
upper = int(input("Ending Number:"))
#
print("Prime numbers between", lower, "and", upper, "are:")
with open("primenumbers.txt", "a") as file:
    file.write("\n")
    file.write("{}".format(today))
    file.write("\n")
#
start = time.time()

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            with open("primenumbers.txt", "a") as file:
                file.write("\n")
                file.write("{}".format(num))
end = time.time()
print(end - start)
