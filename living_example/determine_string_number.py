#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/17 9:37
# @Author   : huyx
# @Site     : 
# @File     : determine_string_number.py
# @Software : PyCharm

# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(s)
#         return True
#     except (TypeError, ValueError):
#         pass
#
#     return False
#
# # 测试字符串和数字
# print(is_number('foo'))
# print(is_number('1'))
# print(is_number('1.3'))
# print(is_number('-1.37'))
# print(is_number('1e3'))
#
# # 测试 Unicode
# # 阿拉伯语 5
# print(is_number('٥'))  # True
# # 泰语 2
# print(is_number('๒'))  # True
# # 中文数字
# print(is_number('四')) # True
# print(is_number('五')) # True
# # 版权号
# print(is_number('©'))  # False


# 扩展到全角函数
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    import unicodedata
    try:
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    if len(s) < 2:
        return False

    try:
        d = 0
        if s.startswith('-'):
            s = s[1:]
        for c in s:
            if c == '-':  # 全角减号
                return False

            if c == '. ':  # 全角点号
                if d > 0:
                    return False
                else:
                    d = 1
                    continue
            unicodedata.numeric(c)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 测试字符串和数字
print(f'{is_number("foo")}')
print(f'{is_number("1")}')
print(f'{is_number("1.3")}')
print(f'{is_number("-1.37")}')
print(f'{is_number("1e3")}')
print(f'{is_number("2.345.6")}')
print(f'{is_number("-5.2-8")}')
print(f'{is_number("52-8")}')
print(f'{is_number("-.5")}')
print(f'{is_number("-5.")}')
print(f'{is_number(".5")}')

# 测试Unicode
# 阿拉伯语 5
print(f'{is_number("٥") }')
# 泰语 2
print(f'{is_number("๒") }')
# 中文数字
print(f'{is_number("四") }')
print(f'{is_number("四卅") }')
# 全角数字
print(f'{is_number("１２３") }')
print(f'{is_number("-１２３") }')
print(f'{is_number("－１２３") }')
print(f'{is_number("１２－３") }')
print(f'{is_number("１２３－") }')
print(f'{is_number("１.２３") }')
print(f'{is_number("１．２３") }')
print(f'{is_number("．２３") }')
print(f'{is_number("－．２３") }')
print(f'{is_number("１．23") }')
print(f'{is_number("１．２．３") }')
# 版权号
print(f'{is_number("©") }')