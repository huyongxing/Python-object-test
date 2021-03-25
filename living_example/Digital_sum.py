#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/16 11:25
# @Author   : huyx
# @Site     : 
# @File     : Digital_sum.py
# @Software : PyCharm

# 用户输入数字
# num1 = input('输入第一个数字：')
# num2 = input('输入第二个数字：')
#
# # 求和
# sum = float(num1) + float(num2)
#
# # 显示计算结果
# print(sum)

# # 合并为一行代码计算
# print('两数之和为 %.1f' %(float(input('输入第一个数字：'))+float(input('输入第二个数字：'))))

# 报错重新输入处理
while 1:
    x = input("请输入数字x的值：")
    y = input("请输入数字y的值：")
    try:
        sum = float(x)+float(y)
    except:
        print("输入的数字格式不正确，请重新输入！")
        continue
    else:
        print(f"两个数字之和为：{sum:.2f}")
        break