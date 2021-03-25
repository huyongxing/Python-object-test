#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/22 9:48
# @Author   : huyx
# @Site     : 
# @File     : name_function.py
# @Software : PyCharm

def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
