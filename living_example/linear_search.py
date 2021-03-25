#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/18 15:33
# @Author   : huyx
# @Site     : 
# @File     : linear_search.py
# @Software : PyCharm

# def search(arr, n, x):
#     for i in range(1, n):
#         if (arr[i] == x):
#             return i
#     return -1
#
#
# # 在数组 arr 中查找字符 D
# arr = ['A', 'B', 'C', 'D', 'E', 'F']
# x = 'D'
# n = len(arr)
# result = search(arr, n, x)
# if (result == -1):
#     print("元素不在数组中")
# else:
#     print("元素在数组中的索引为：", result)

def LinearSearch(list):
    num = int(input('Number:\t'))
    counter = 0
    null = 0

    for i in list:
        if i == num:
            print('Find number {} in place {}.'.format(num, counter))
        else:
            null += 1
        counter += 1
    if null == counter:
        print('Don\`t find it.')


list = [1, 2, 5, 7, 8, 35, 567, -1, 0, -3, -9]
LinearSearch(list)
