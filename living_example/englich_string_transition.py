#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/18 17:01
# @Author   : huyx
# @Site     : 
# @File     : englich_string_transition.py
# @Software : PyCharm

# # 字符串大小写问题关于英文字符串的大小写转换
#
# # 首字母大写
# a = 'hello world!,zHong yUan GoNg!'
# print(a.title())
#
# # 全部大写
# print(a.upper())
#
# # 全部小写
# print(a.lower())
#
# # 首个单词的首字母大写
# print(a.capitalize())

# # 将字符串"ilovechina"进行反转的方法写出来
# s1 = "ilovechina"
#
# # [:: -1]是对字符串的截取操作，[-1]是取倒数第一个元素
# print(s1[:: -1])
#
# print(s1[:3])   #从 0 开始截取三个元素
# print(s1[3:])   #从 3 开始截取元素
# print(s1[::])
# print(s1[3])    #截取第 3 个元素
# print(-3)   #截取倒数第三个元素

# python中的字符串格式化方式($s, format, fstring(python3.6开始才支持，现在推荐的写法))

# # 通过位置格式化
# print('hello,{0}{1}{2}'.format('zhong', 'yuan', 'gong'))
#
# # 通过 key 填充
# print('hell,{name},my name is {self}!!'.format(name='tom', self='sir'))

# # 通过数组的下标填充
# n = ['tom', 'str']
# print('hello,{n[0]},my name is {n[1]}!!'.format(n=1))

# # 通过字典的 key 填充，键名不加引号
# m = {'name':'tom', 'self':'sir'}
# print('hell,{m[name]},my name is {m[self]}!!'.format(m=m))

# # 去除掉字符串 " adabdw " 的前后空格
# def strip_function(s1):
#     return s1.strip()
#
# s1 = " adabdw "
# print(strip_function(s1))

# # 删除字符串中的空格集中函数
# c = ' hello world!!! '
#
# # 去掉字符串开头和末尾的空格
# print(c.strip())
# # 去掉字符串左边的空格
# print(c.lstrip())
# # 去掉字符串右边的空格
# print(c.rstrip())
# # 去掉字符串中所有的空格
# print(c.replace(' ',''))

# 生成一个有N个元素的由随机数n组成的列表，其中N和n的取值范围为（1< N <= 100）和（0 <= n <= 2的31次方减一）。然后再随机从这个列表中取N（1<= N <= 100）个随机数出来并排序，然后显示。
# random模块中有一个关于整数随机数的生成函数为random.randrange(start, stop[, step])生成n和N都要用到这个随机函数。

# import random
#
# N = random.randrange(2, 101)
# print('总共会生成%d个随机数' % N)
# L = []
# for x in range(N):
#     y = random.randrange(0, pow(2, 31) - 1)
#     print('生成的随机数为：' + str(y))
#     L.append(y)
#
# L1 = []
# n = random.randrange(1, N)
# print('从生成的随机数中选取%d个随机数' % n)
# for z in range(n):
#     l = random.randrange(1, n)
#     m = L[l]
#     L1.append(m)
#     print('选取的随机数为：' + str(m))
#
# print('进过排序后的列表为：', end = '')
# print(sorted(L1))

# # 小学生练习10以内的加法
# # 随机生成加减乘除题目;
# # 学生查看题目并输入答案
# # 判别学生答题是否正确?
# # 退出时, 统计学生答题总数,正确数量及正确率(保留两位小数点)
#
# import random  # 调用随机数模块
#
# count = 0  # 初始化变量总数count为0
# right = 0  # 初始化变量正确个数right为0
# while True:  # 为真时进入循环
#     a = random.randrange(0, 9)  # 变量a为随机整数0-9
#     b = random.randrange(1, 9)  # 做除数时不能取0
#     op = ['+', '-', '*', '/']  # op为运算符号列表
#     d = random.choice(op)  # 随机选择运算符赋给变量d
#     print('%d %s %d = ' % (a, d, b))  # 打印出随机生成的提
#     question = input('请输入您的答案：')
#     result1 = a + b
#     result2 = a - b
#     result3 = a * b
#     result4 = a / b
#
#     if question == str(result1) and d == '+':
#         print('回答正确')
#         right += 1
#         count += 1
#     elif question == str(result2) and d == '-':
#         print('回答正确')
#         right += 1
#         count += 1
#     elif question == str(result3) and d == '*':
#         print('回答正确')
#         right += 1
#         count += 1
#     elif question == str(result4) and d == '/':
#         print('回答正确')
#         right += 1
#         count += 1
#     elif question == 'q':
#         break
#     else:
#         print('回答错误')
#         count += 1
#
# percent = right / count
# print('测试结束，共回答%d道题，正确个数为%d，正确率为%.2f%%' % (count, right, percent * 100))

# import random
#
# right = 0  # 正确题目数量
# cycle = 0  # 控制循环次数
# while True:
#     cycle += 1
#     po = ['+']
#     Fuhao = random.choice(po)
#     Num1 = random.randint(0, 10)
#     Num2 = random.randint(0, 10)
#     print('%.d+%.d=?' % (Num1, Num2))
#     Answer = int(input('请输入答案：'))
#     Correct_Answer = Num1 + Num2
#     if Answer == Correct_Answer:
#         print('正确！')
#         right += 1
#     else:
#         print('错误！')
#         Choice = input('是否要退出？退出【1】继续答题【2】')
#         if Choice == '1':
#             break
# k = (right / cycle * 100)
# print('已经答了%d道题目' % cycle)
# print('正确题目数量：%d' % right)
# print('正确率：%.2f%%' % k)

# python实现从1加到10的三种方法：for循环，while循环，导入模块发

# 第一种是for循环：
# def sumStartToEnd(start,end):
#     sum = 0
#     for n in range(start,end+1,1):
#         sum = sum + n
#     return sum
# print(sumStartToEnd(1, 10))

# def sum():
#     sum = 0
#     for n in range(1, 10):
#         sum = sum + n
#     return sum
# print(sum())

# 第二种是while循环：
# def sum():
#     sum = 0
#     x = 1
#     while x < 11:
#         sum = sum + x
#         x += 1
#     return sum
# print(sum())
#
# count = 1
# number = 0
# while count <= 10:
#     number += count
#     count += 1
# print(number)

# 第三种导入模块的内建函数reduce
# def sum(x, y):
#     return x + y
# from functools import reduce
# print(reduce(sum, range(1,11)))

