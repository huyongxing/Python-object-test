#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/12 11:08
# @Author   : huyx
# @Site     : 
# @File     : file_download.py
# @Software : PyCharm

# HTTP 头部
print("Content-Disposition: attachment; filename=\"账号.txt\"")
print()

# 打开文件
fo = open("账号.txt", "rb")

str = fo.read()
print(str)

# 关闭文件
fo.close()