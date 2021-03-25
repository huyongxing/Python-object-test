# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2020/4/1 10:55
# @Author   : Aidan
# @Site     :
# @File     : test1.PY
# @Software : PyCharm

# message = "Hello Python world!"
# print(message)

# message = "Hello Python Crash Course world!"
# print(message)

# message = "Hello Python Crash Course world!"
# print(mesage) #输出变量名错误

# mesage = "Hello Python Crash Course world!"
# print(mesage)   #变量拼写错误依然执行成功

# simple_message = "What are you doing?"
# print(simple_message)   #练习输出带下划线的变量

# message = input("Input message: ")
# print(message)

# simple_message = input("What are you doing: ")
# print(simple_message)   #练习将消息储存到变量中打印出来，再将变量的值修改为一条新消息，并打印出来

# "This is a string."
# "This is also a string."
# 'I told my friend, "Python is my favorite language!"'
# "The language 'Python' is named after Monty Python, not the snake."
# "One of Python's strengths is its diverse and supportive community."

# name = "ada lovelace"
# print(name.title()) #title()函数，将字符串的首字母改为大写

# name = "ADA"
# print(name.title()) #ADA同Ada

# name = "Ada Lovelace"
# print(name.upper()) #upper()函数，将字符串改为全部大写
# print(name.lower()) #lower()函数，将字符串改为全部小写

# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " +last_name
# print(full_name)    #使用加号（+）来合并字符串

# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# print("Hello, " + full_name.title() + "!")  #将字符串拼接为一条格式良好的问候语

# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# message = "Hello," + full_name.title() + "!"
# print(message)  #把整条信息都储存在一个变量中

# import random
# i = random.choice(["赵","钱","孙","李","周","吴","郑","王","冯","陈","褚","卫","蒋"])
# j = random.choice(["伟","刚","勇","毅","俊","峰","强","军","平","保","东","文","辉","力","明","永","健","世","广","志","义"])
# name = i + j
# print(name)     #随机选取字符串输出

# print("Python")
# print("\tPython")   #制表符“\t”
# print("\nPython")   #换行符“\n”
# print("Languages:\nPython\nC\nJavaScript")   #字符串中添加换行符“\n”
# print("Languages:\n\tPython\n\tC\n\tJavaScript")    #字符串中添加换行符“\n”和制表符“\t”

# favorite_language = 'python '
# print(favorite_language)
# print(favorite_language.rstrip())   #rstrip()方法移除右边的空格

# favorite_language = ' python'
# print(favorite_language.lstrip())   #lstrip()方法移除左边的空格

# favorite_language = ' python '
# print(favorite_language.strip())    #strip()方法同时移除两端的空格

# favorite_language = 'python '
# favorite_language = favorite_language.rstrip()
# print(favorite_language)    #先将删除操作的结果存会到变量中,这样输出的变量永远没有空格

# message = "One of Python's strengths is its diverse community."
# message = 'One of Python's strengths is its diverse community.' #字符串语法错误
# print(message)

# name_cases = "eric"
# Name = name_cases.title()
# print("Hello " + Name + ", " + "would you like to learm some Python today?")    #将姓名存到变量中,并向用户显示一条消息

# def function():
# 	print('This is a function')
# 	a = 1+2
# 	print(a)    #def函数

"""loan_money：贷款金额合计=实际贷款额+实际贷款额×（总利率-分期手续费率）"""
"""contract_loan_money:实际贷款额"""
"""sf_money:首付金额=车辆价格-贷款金额合计"""
"""sf_proportion:首付比例=首付金额/车辆价格*100%"""

# print(2 + 3)    #加
# print(3 - 2)    #减
# print(2 * 3)    #乘
# print(3 / 2)    #除
# print(3 ** 2)   #乘方
# print(3 ** 3)
# print(10 ** 6)
# print(2 + 3 * 4)
# print((2 + 3) * 4)
# print(0.1 + 0.1)
# print(0.2 + 0.2)
# print(2 * 0.1)
# print(2 * 0.2)
# print(0.2 + 0.1)    #浮点数结果包含小数位数可能是不确定的
# print(3 * 0.1)

#类型错误
# age = 23
# message = "Happy " + age + "rd Birthday!"
# print(message)

#str()将23转换为字符串
# age = 23
# message = "Happy " + str(age) + "rd Birthday!"
# print(message)

# print(3 / 2)
# print(3.0 / 2)
# print(3 / 2.0)
# print(3.0 / 2.0)

# 最喜欢的数字
# numbers = 9
# message = "My favorite number is " + str(numbers)
# print(message)

# print("Hello Python people!")
# import this

#列表
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[2])
# print(bicycles[3])
# print(bicycles[-1])

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = "My first bicycle was a " + bicycles[0].title() + "."
# print(message)

# commuters = ['walk', 'bicycle', 'honda motorcycle', 'automobile']
# message = "I would like to own a " + commuters[2].title()
# print(message)

# Python比较运算符
# a = 21
# b = 10
# c = 0
# if  a == b :
#     print("1 - a 等于 b")
# else:
#     print("1 - a 不等于 b")
#
# if a != b :
#     print("2 - a 不等于 b")
# else:
#     print("2 - a 等于 b")
#
# if a < b :
#     print("3 - a 小于 b")
# else:
#     print("3 - a 大于等于 b")
#
# if a > b :
#     print("4 - a 大于 b")
# else:
#     print("4 - a 小于等于 b")
#
# # 修改变量a和b的值
# a = 5
# b = 20
# if a <= b :
#     print("5 - a 小于等于 b")
# else:
#     print("5 - a 大于 b")
#
# if b >= a :
#     print("6 - b 大于等于 a")
# else:
#     print("6 - b 小于 a")

# # Python赋值运算符
# a = 21
# b = 10
# c = 0
#
# c = a + b
# print("1 - c 的值为：", c)
#
# c += a
# print("2 - c 的值为：", c)
#
# c *= a
# print("3 - c 的值为：", c)
#
# c /= a
# print("4 - c 的值为：", c)
#
# c = 2
# c %= a
# print("5 - c 的值为：", c)
#
# c **= a
# print("6 - c 的值为：", c)
#
# c //= a
# print("7 - c 的值为：", c)

# # Python位运算符
# a = 60          #60 = 0011 1100
# b = 13          #13 = 0000 1101
# c = 0
#
# c = a & b;      #12 = 0000 1100
# print("1 - c 的值为：", c)
#
# c = a | b;      #61 = 0011 1101
# print("2 - c 的值为：", c)
#
# c = a ^ b;      #49 = 0011 0001
# print("3 - c 的值为：", c)
#
# c = ~a;         #-61 = 1100 0011
# print("4 - c 的值为：", c)
#
# c = a << 2;     #240 = 1111 0000
# print("5 - c 的值为：", c)
#
# c = a >> 2;     #15 = 0000 1111
# print("6 - c 的值为：", c)

# # Python逻辑运算符
# a = 10
# b = 20
#
# if a and b :
#     print("1 - 变量 a 和 b 都为true")
# else:
#     print("1 - 变量 a 和 b 有一个不为 true")
#
# if a or b :
#     print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#     print("2 - 变量 a 和 b 都不为 true")

# #修改变量a 的值
# a = 0
# if a and b :
#     print("3 - 变量 a 和 b 都为 true")
# else:
#     print("3 - 变量 a 和 b 有一个不为 true")
#
# if a or b :
#     print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#     print("4 - 变量 a 和 b 都不为 true")
#
# if not( a and b ):
#     print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
# else:
#     print("5 - 变量 a 和 b 都为 true")

# # Python成员运算符
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5];
#
# if ( a in list ):
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")
#
# if ( b not in list ):
#     print("2 - 变量 b 不在给定的列表中 list 中")
# else:
#     print("2 - 变量 b 在给定的列表中 list 中")
#
# #修改变量 a 的值
# a = 2
# if ( a in list ):
#     print("3 - 变量 a 在给定的列表中 list 中")
# else:
#     print("3 - 变量 a 不在给定的列表中 list 中")

# #Python身份运算符
# a = 20
# b = 20
#
# if ( a is b ):
#     print("1 - a 和 b 有相同的标识")
# else:
#     print("1 - a 和 b 没有相同的标识")
#
# if ( a is not b ):
#     print("2 - a 和 b 没有相同的标识")
# else:
#     print("2 - a 和 b 有相同的标识")
#
# #修改变量 b 的值
# b = 30
# if ( a is b ):
#     print("3 - a 和 b 有相同的标识")
# else:
#     print("3 - a 和 b 没有相同的标识")
#
# if ( a is not b ):
#     print("4 - a 和 b 没有相同的标识")
# else:
#     print("4 - a 和 b 有相同的标识")

# # Python运算符优先级
# a = 20
# b = 10
# c = 15
# d = 5
# e = 0
#
# e = (a + b) * c / d         #(30 * 15) / 5
# print("(a + b) * c / d 运算结果为：", e)
#
# e = ((a + b) * c) / d       #(30 * 15) / 5
# print("((a + b) * c) / d 运算结果为：", e)
#
# e = (a + b) * (c / d);      #(30) * (15/5)
# print("(a + b) * (c / d) 运算结果为：", e)
#
# e = a + (b * c) / d;        #20 + (150/5)
# print("a + (b * c) / d 运算结果为：", e)

# Python条件语句
# if 判断条件：
#     执行语句···
# else：
#     执行语句···
#
# a = 1
# while a < 7 :
#     if(a % 2 == 0):
#         print(a, "is even")
#     else:
#         print(a, "is odd")
#     a += 1

# flag = False
# name = 'luren'
# if name == 'python':           #判断变量是否为 python
#     flag = True                #条件成立时设置标志为真
#     print('welcome boss')      #并输出欢迎信息
# else:
#     print(name)                #条件不成立时输出变量名称

# num = 5
# if num == 3:                     #判断num的值
#     print('boss')
# elif num == 2:
#     print('user')
# elif num == 1:
#     print('worker')
# elif num < 0:                    #值小于零食输出#
#     print('error')
# else:
#     print('roadman')             #条件均不成立时输出

# num = 9
# if num >= 0 and num <= 10:         #判断值是否在0~10之间
#     print('hello')
#
# num == 10
# if num < 0 or num >10:             #判断值是否在小于0或大于10
#     print('hello')
# else:
#     print('undefine')
#
# num = 8
# if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    #判断值是否在0~5或者10~15之间
#     print('hello')
# else:
#     print('undefine')

# var = 100
# if ( var == 100 ) : print("变量 var 的值为100")
# print("Good bye!")
#
# var = 99
# if ( var == 100 ) : print("变量 var 的值为100")
# print("Good bye!")

#Python While循环语句
# a = 1
# while a < 10:
#     print(a)
#     a += 2

# numbers = [12, 37, 5, 42, 8, 3]
# even = []
# odd = []
# while len(numbers) > 0 :
#     number = numbers.pop()
#     if(number % 2 == 0):
#         even.append(number)
#     else:
#         odd.append(number)
# print(even)

# count = 0
# while (count < 9):
#     print("The count is:", count)
#     count = count + 1
# print("Good bye!")

# i = 1
# while i < 10:
#     i += 1
#     if i%2 > 0:             #非双数时跳过输出
#         continue
#     print(i)                #输出双数2、4、6、8、10

# i = 1
# while 1:                      #循环条件为1必定成立
#     print(i)                  #输出1~10
#     i += 1
#     if i > 10:                #当i大于10时跳出循环
#         break

# 无限循环
# var = 1
# while var == 1 :                #该条件永远为true，循环将无限执行下去
#     num = input("Enter a number :")
#     print("You entered: ", num)
#
# print("Good bye!")

# 循环使用else语句
# count = 0
# while count < 5:
#     print(count, "is less than 5")
#     count = count + 1
# else:
#     print(count, "is not less than 5")

# 简单语句组
# flag = 1
# while (flag): print('Given flag is really true!')
# print("Good bye!")

# Python for 循环语句
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# for循环的语法格式如下：
# for iterating_var in sequence:
#     statements(s)

# for letter in 'Python':           #第一个实例
#     print('当前字母：', letter)

# fruits = ['banana', 'apple', 'mango']
# for fruit in fruits:                #第二个实例
#     print('当前水果：', fruit)

# 通过序列索引迭代循环
# fruits = ['banana', 'apple', 'mango']
# for index in range(len(fruits)):
#     print('当前水果：', fruits[index])

# 循环使用else语句
# 在Python中，for...else表示这样的意思，for中的语句和普通的没有区别，else中的语句会在循环正常执行完（即for不是通过break跳出而中断的）的情况下执行，while...else也是一样。
# for num in range(10,20):            #迭代10到20之间的数字
#     for i in range(2,num):          #根据因子迭代
#         if num%i == 0:              #确定第一个因子
#             j=num/i                 #计算第二个因子
#             print('%d 等于 %d * %d' % (num,i,j))
#             break                   #跳出当前循环
#     else:                           #循环的else部分
#         print(num, '是一个质数')

# Python循环嵌套
# Python语言允许在一个循环体里面嵌套另一个循环。
# Python for循环嵌套语法：
# for iterating_var in sequence:
#     for iterating_var in sequence:
#         statements(s)
#     statements(s)

# Python while循环嵌套语法：
# while expression:
#     while expression:
#         statement(s)
#     statement(s)

# while循环中可以嵌入for循环，反之for循环中可以嵌入while循环
# i = 2
# while(i < 100):
#     j = 2
#     while(j <= (i/j)):
#         if not(i%j): break
#         j = j + 1
#     if (j > i/j) : print(i, "是素数")
#     i = i + 1

# Python break语句
# Python break语句，就像在C语言中，打破了最小封闭for或while循环。
# break语句用来终止循环语句，即循环条件没有false条件或者序列还没被完全递归完，也会停止执行循环语句。
# break语句用在while和for循环中。
# 如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。
# Python语句break语句语法：
# break
# for letter in 'Python':             #第一个实例
#     if letter == 'h':
#         break
#     print('当前字母：', letter)

# var = 10                              #第二个实例
# while var > 0:
#     print('当前变量值：', var)
#     var = var - 1
#     if var == 5:                      #当变量var等于5时退出循环
#         break

# Python continue语句
# Python continue语句跳出本次循环，而break跳出整个循环。
# continue语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# continue语句用在while和for循环中。
# Python语言continue语句语法格式如下：
# continue

# for letter in 'Python':                 #第一个实例
#     if letter == 'h':
#         continue
#     print('当前字母：', letter)

# var = 10                                    #第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:
#         continue
#     print('当前变量值：', var)

# Python pass语句
# Python pass是空语句，是为了保持程序结构的完整性。
# pass不作任何事情，一般用做占位语句。
# Python语言pass语句语法格式如下：
# pass

# for letter in 'Python':
#     if letter == 'h':
#         pass
#         print('这是pass块')
#     print('当前字母：', letter)

# pass一般用于占位置
# 在Python中有时候会看到一个def函数：
# def sample(n_sample):
#     pass

# 该处的pass便是占据一个位置，因为如果定义一个空函数程序会报错，当你没有想好函数的内容是可以用pass填充，使程序可以正常运行
# 在Python3.x的时候pass可以写或不写。

# Python2.x:
# def function():
#     #空函数在Python2.x版本中pass是必须的
#     pass

# Python3.x：
# def function():
#     #在Python3.x的时候pass可以写或不写
#     pass

# Python Number(数字)
# Python Number数据类型用于存储数值
# 数据类型是不允许改变的，这就意味着如果改变Number数据类型的值，将重新分配存储空间。

# Python Number类型转换
# int(x [,base ])                 将 x 转换为一个整数
# long(x [,base ])                将 x 转换为一个长整数
# float(x )                       将 x 转换到一个浮点数
# complex(real [,imag ])          创建一个复数
# str(x )                         将对象 x 转换为字符串
# repr(x )                        将对象 x 转换为表达式字符串
# eval(str )                      用来计算在字符串中的有效Python表达式，并返回一个对象
# tuple(s )                       将序列 s 转换为一个元组
# list(s )                        将序列 s 转换为一个列表
# chr(x )                         将一个整数转换为一个字符
# unichr(x )                      将一个整数转换为Unicode字符
# ord(x )                         将一个字符转换为它的整数值
# hex(x )                         将一个整数转换为一个十六进制字符串
# oct(x )                         将一个整数转换为一个八进制字符串

# Python math模块、cmath模块
# Python中数学运算常用的函数基本都在math模块、cmath模块中。
# Python math模块提供了许多对浮点数的数学运算函数。
# Python cmath模块包含了一些用于复数运算的函数。
# cmath模块的函数跟math模块函数基本一致，区别是cmath模块运算的是复数，math模块运算的是数学运算。
# 要使用math或cmath函数必须先导入：
# import math
# dir(math)

# Python数字函数
# abs(x)                          返回数字的绝对值，如abs(-10)返回10
# ceil(x)                         返回数字的上入整数，如math.ceil(4.1)返回5
# cmp(x, y)                       如果x < y返回-1，如果x == y 返回0，如果x > y返回1
# exp(x)                          返回e的x次幂(e^x)，如math.exp(1)返回2.718281828459045
# fabs(x)                         返回数字的绝对值，如math.fabs(-10)返回10.0
# floor(x)                        返回数字的下舍整数，如math.floor(4.9)返回4
# log(x)                          如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)                        返回以10为基数的x的对数，如math.log10(100)返回2.0
# max(x1,x2,...)                  返回给定参数的最大值，参数可以为序列
# min(x1,x2,...)                  返回给定参数的最小值，参数可以为序列
# modf(x)                         返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
# pow(x,y)                        x**y运算后的值
# round(x[,n])                    返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
# sqrt(x)                         返回数字x的平方根

# Python随机数函数
# 随机数可以用于数字，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
# choice(seq)                     从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个调整。
# randrange([start,]stop[,step])  从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为1
# random()                        随机生成下一个实数，它在[0,1)范围中。
# seed([x])                       改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮助你选择seed。
# shuffle(lst)                    将序列的所有元素随机排序
# uniform(x, y)                   随机生成下一个实数，它在[x,y)范围中

# Python三角函数
# acos(x)                         返回x的反余弦弧度值
# asin(x)                         返回x的反正弦弧度值
# atan(x)                         返回x的反正切弧度值
# atan2(y, x)                     返回给定的x及y坐标值的反正切值
# cos(x)                          返回x的弧度的余弦值
# hypot(x, y)                     返回欧几里德范数sqrt(x*x + y*y)
# sin(x)                          返回的x弧度的正弦值
# tan(x)                          返回x弧度的正切值
# degrees(x)                      将弧度转换为角度，如degrees(math.pi/2)，返回90.0
# radians(x)                      将角度转换为弧度

# Python数学常量
# pi                              数学常量pi（圆周率，一般以π来表示）
# e                               数学常量e, e即自然常数（自然常数）

# Python字符串
# 字符串是Python中最常用的数据类型。可以使用引号（“或”）来创建字符串
# 创建字符串很简单，只要为变量分配一个值即可。
# var1 = 'Hello World!'
# var2 = "Python Runoob"

# Python访问字符串中的值
# Python不支持单字符类型，单字符在Python中也是作为一个字符串使用
# Python访问子字符串，可以使用方括号来截取字符串
# var1 = 'Hello World!'
# var2 = "Python Runoob"
#
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])

# Python字符串连接
# 可以对字符串进行截取并与其他字符串进行连接
# var1 = 'Hello World!'
# print("输出：-", var1[:6] + 'Runood!')

# Python转义字符
# 在需要在字符中使用特殊字符时，python用反斜杠 \ 转义符
# \(在行尾时)                     续行符
# \\                              反斜杠符号
# \'                              单引号
# \"                              双引号
# \a                              响铃
# \b                              退格(Backspace)
# \e                              转义
# \000                            空
# \n                              换行
# \v                              纵向制表符
# \t                              横向制表符
# \r                              回车
# \f                              换页
# \oyy                            八进制数，y代表0~7的字符，例如：\012代表换行
# \xyy                            十六进制数，以\x开头，yy代表的字符，例如：\x0a代表换行
# \other                          其它的字符以普通格式输出

# Python字符串运算符
# +                               字符串连接
# *                               重复输出字符串
# []                              通过索引获取字符串中字符
# [:]                             截取字符串中的部分
# in                              成员运算符-如果字符串中包含给定的字符返回True
# not in                          成员运算符-如果字符串中不包含给定的字符返回True
# r/R                             原始字符串-原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。原始字符串出在字符串的第一个引号前加上字母“r”（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# %                               格式字符串

# a = "Hello"
# b = "Python"
#
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4]输出结果：", a[1:4])
#
# if("H" in a):
#     print("H在变量a中")
# else:
#     print("H不在变量a中")
#
# if("M" not in a):
#     print("M不在变量a中")
# else:
#     print("M在变量a中")
#
# print(r'\n')
# print(R'\n')

# Python字符串格式化
# Python支持格式化字符串的输出。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符%s的字符串中。
# 在Python中，字符串格式化使用 C 中的sprintf函数一样的语法。
# print("My name is %s and weight is %d kg!" % ('Zara', 21))

# %c                              格式化字符及其ASCII码
# %s                              格式化字符串
# %d                              格式化整数
# %u                              格式化无符号整型
# %o                              格式化无符号八进制数
# %x                              格式化无符号十六进制数
# %X                              格式化无符号十六进制数（大写）
# %f                              格式化浮点数字，可指定小数点后的精度
# %e                              用科学计数法格式化浮点数
# %E                              作用同%e，用科学计数法格式化浮点数
# %g                              %f和%e的简写
# %G                              %F和%E的简写
# %p                              用十六进制数格式化变量的地址

# *	                            定义宽度或者小数点精度
# -	                            用做左对齐
# +	                            在正数前面显示加号( + )
# <sp>	                        在正数前面显示空格
# #	                            在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0	                            显示的数字前面填充'0'而不是默认的空格
# %	                            '%%'输出一个单一的'%'
# (var)	                        映射变量(字典参数)
# m.n.	                        m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

# Python三引号
# Python中三引号可以将复杂的字符串进行赋值
# Python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
# 三引号的语法是一对连续的单引号或者双引号（通常都是成对的用）

# Python的字符串内建函数
# string.capitalize()                                     把字符串的第一个字符大写
# string.center(width)                                    返回一个原字符串居中，并使用空格填充至长度width的新字符串
# string.count(str,beg=0,end=len(string))                 返回str在string里面出现的次数，如果beg或者end指定则返回指定范围内str出现的次数
# string.decode(encoding='UTF-8',errors='strict')         以encoding指定的编码格式解码string，如果出错默认报一个ValueErrord的异常，除非errors指定的是'ignore'或者'replace'
# string.encode(encoding='UTF-8',errors='strict')         以encoding指定的编码格式解码string，如果出错默认报一个ValueError的异常，除非errors指定的是'ignore'或者'replace'
# string.endswith(obj,beg=0,end=len(string))              检查字符串是否以obj结束，如果beg或者end指定则检测指定的范围内是否以obj结束，如果是，返回True，否则返回False
# string.expandtabs(tabsize=8)                            把字符串string中的tab符号转为空格，tab符号默认的空格数是8
# string.find(str,beg=0,end=len(string))                  检测str是否包含在string中，如果beg和end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
# string.format()                                         格式化字符串
# string.index(str,beg=0,end=len(string))                 跟find()方法一样，只不过如果str不在string中会报一个异常
# string.isalnum()                                        如果string至少有个字符并且所有字符都是字母或数字则返回True，否则返回False
# string.isalpha()                                        如果string至少有一个字符并且所有字符都是字母则返回True，否则返回False
# string.isdecimal()                                      如果string只包含十进制数字则返回True否则返回False
# string.isdigit()                                        如果string只包含数字则返回True否则返回False
# string.islower()                                        如果string中包含至少一个区分大小写的字符，并且所有这些（区分大小写的）字符都是小写，则返回True，否则返回False

# Python列表(List)
# 访问列表中的值
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
#
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])

# 更新列表
# list = []                       ##空列表
# list.append('Google')           ##使用append()添加元素
# list.append('Runoob')
# print(list)

# 删除列表元素
# list1 = ['physice', 'chemistry', 1977, 2000]
# print(list1)
# del list1[2]
# print("After deleting value at index 2 : ")
# print(list1)

# Python列表脚本操作符
# 列表对+和*的操作符与字符串相似。+号用于组合列表，*号用于重复列表。
# len([1, 2, 3])                  结果：3                                描述：长度
# [1, 2, 3]+[4, 5, 6]             结果：[1,2,3,4,5,6]                    描述：组合
# ['Hi!']*4                       结果：['Hi!', 'Hi!', 'Hi!', 'Hi!']     描述：重复
# 3 in[1, 2, 3]                   结果：True                             描述：元素是否存在与列表中
# for x in[1, 2, 3]: print(x)     结果：1 2 3                            描述：迭代

# Python列表截取
# L = ['Google', 'Runoob', 'Taobao']
# print(L[2])
# print(L[-2])
# print(L[1:])

# Python列表函数&方法
# Python包含以下函数：
# cmp(list1, list2)                   比较两个列表的元素
# len(list)                           列表元素个数
# max(list)                           返回列表元素最大值
# min(list)                           返回列表元素最小值
# list(seq)                           将元祖转换为列表

# Python包含以下方法：
# list.append(obj).                    在列表末尾添加新的对象
# list.count(obj).                     统计某个元素在列表中的出现次数
# list.extend(seq).                    在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj).                     从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj).             将对象插入列表
# list.pop([index=-1]).                移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj).                    移除列表中某个值的第一个匹配项
# list.reverse().                      反向列表中的元素
# list.sort(cmp=None, key=None, reverse=False)    对原列表进行排序

# Python元组
# Python的元组与列表类似，不同之处在于元祖的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元祖创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 如下实例：
# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5)
# tup3 = "a", "b", "c", "d"

# 创建空元组
# tup1 = ()

# 元组中只包含一个元素时，需要在元素后面添加逗号
# tup1 = (50,)

# 访问元组
# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7)
# print("tup1[0]: ", tup1[0])
# print("tup2[1:5]: ", tup2[1:5])

# # 修改元祖
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
#
# # 以下修改元祖元素操作是非法的
# # tup1[0] = 100
#
# # 创建一个新的元祖
# tup3 = tup1 + tup2
# print(tup3)

# 删除元祖
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元祖
# tup = ('physics', 'chemistry', 1997, 2000)
# print(tup)
# del tup
# print("After deleting tup : ")
# print(tup)

# 元组运算符
# 与字符串一样，元组之间可以使用+号和*号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
# len((1, 2, 3))                                  结果：3                                描述：计算元素个数
# (1, 2, 3)+(4, 5, 6)                             结果：(1, 2, 3, 4, 5, 6)               描述：连接
# ('Hi!',)*4                                      结果：('Hi!', 'Hi!', 'Hi!', 'Hi!')     描述：复制
# 3 in(1, 2, 3)                                   结果：True                             描述：元素是否存在
# for x in(1, 2, 3):print(x)                      结果：1 2 3                            描述：迭代

# 元组索引，截取
# 因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
# L = ('spam', 'Spam', 'SPAM')

import time

# ticks = time.time()
# print("当前时间戳为：", ticks)

# 获取当前时间
# localtime = time.localtime(time.time())
# print("本地时间为：", localtime)

# 获取格式化的时间
# localtime = time.asctime( time.localtime(time.time()) )
# print("本地时间为：", localtime)

# 格式化日期
# 格式化成2021-03-01 09:01:08形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Mon Mar 01 09:26:24 2021形式
# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
# a = "Mon Mar 01 09:26:24 2021"
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))
# 获取某月日历
# import calendar
# cal = calendar.month(2021, 3)
# print("以下输出2021年3月份的日历：")
# print(cal)

# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常！！")
# except IOError:
#     print("Error:没有找到文件或读取文件失败！")
# else:
#     print("内容写入文件成功")
#     fh.close()

# try-finally 语句
# try-finally 语句无论是否发生异常都将执行最后的代码。
# try:
# <语句>
# finally:
# <语句>        #退出try时总会执行
# raise

# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常！！")
# finally:
#     print("Error: 没有找到文件或读取文件失败")

# try:
#     fh = open("testfile", "w")
#     try:
#         fh.write("这是一个测试文件，用于测试异常！！")
#     finally:
#         print("关闭文件")
#         fh.close()
# except IOError:
#     print("Error: 没有找到文件或读取文件失败")

# 异常的参数
# 一个异常可以带上参数，可作为输出的异常信息参数。
# 你可以通过except语句来捕获异常的参数，如下所示：
# try:
#     正常的操作
#     ··········
# except ExceptionType, Argument:
#     你可以在这里输出 Argument 的值···
# 变量接受的异常值通常包含在异常的语句中。在元祖的表单中变量可以接收一个或者多个值。
# 元组通常包含错误字符串，错误数字，错误位置。

#定义函数
# def temp_convert(var):
#     try:
#         return int(var)
#     except (ValueError,) as Argument:
#         print("参数没有包含数字\n", Argument)
#
# #调用函数
# temp_convert("xyz");

# 触发异常
# 我们可以使用 raise 语句自己触发异常
# raise 语法格式如下：
# raise [Exception [, args [, traceback]]]
# 语句中 Exception 是异常的类型（例如，NameError)参数标准异常中任一种，args 是自己提供的异常参数。
# 最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。

# 实例
# 一个异常可以是一个字符串，类或对象。Python的内核提供的异常，大多数都是实例化的类，这是一个类的实例的参数。
# 定义一个异常非常简单，如下所示：
def functionName( level):
    if level < 1:
        raise Exception("Invalid level!", level)
        #触发异常后，后面的代码不会再执行
# 注意：为了能够捕获异常，"except"语句必须有用相同的异常来抛出类对象或者字符串。
# 例如我们捕获以上异常，"except"语句如下所示：
# try:
#     正常逻辑
# except Exception,err:
#     触发自定义异常
# else:
#     其余代码

# 实例
# 定义函数
# def mye( level ):
#     if level < 1:
#         raise Exception("Invalid level!", level)
#         # 触发异常后，后面的代码就不会再执行
# try:
#     mye(0)                  #触发异常
# except (Exception,) as err:
#     print(1,err)
# else:
#     print(2)

# 用户自定义异常
# 通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。
# 以下为与RuntimeError相关的实例，实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。
# 在try语句块中，用户自定义的异常后执行except块语句，变量e是用于创建Networkerror类的实例。
# class Networkerror(RuntimeError):
#     def __init__(self, arg):
#         self.args = arg
# # 在你定义以上类后，你可以触发该异常，如下所示：
# try:
#     raise Networkerror("Bad hostname")
# except Networkerror as e:
#     print(e.args)

# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name:", self.name, ", Salary:", self.salary)
# empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
# 第一种方法__init__()方法是一种特殊的方法，被成为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
# self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入响应的参数。

# self代表类的实例，未非类
# 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一参数名称，按照惯例它的名称是sell。
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.prt()
# 从执行结果可以很明显的看出，self代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。
# self不是python关键字，我们把他换成runoob也是可以正常执行的：
# 实例
# class Test:
#     def prt(runoob):
#         print(runoob)
#         print(runoob.__class__)
#
# t = Test()
# t.prt()

# 创建实例对象
# 实例化类其他编程语言中一般用关键字new，但是在Python中并没有这个关键字，类的实例化类似函数调用方式。
# 以下使用类的名称Employee来实例化，并通过__init__方法接收参数。
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)

# 访问属性
# 你可以使用点号 . 来访问对象的属性。使用如下类的名称访问类变量。
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)

# 完整实例
# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name:", self.name, ", Salary:", self.salary)
#
# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)

# 添加，删除，修改类的属性，如下所示：
# emp1.age = 7        #添加一个 'age' 属性
# emp1.age = 8        #修改 'age' 属性
# del emp1.age        #删除 'age' 属性

# 使用以下函数的方式来访问属性：
# getattr(obj, name[, default]) : 访问对象的属性。
# hasattr(obj,name) : 检查是否存在一个属性。
# setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
# delattr(obj, name) : 删除属性。

# hasattr(emp1, 'age')        #如果存在 'age' 属性返回 True。
# getattr(emp1, 'age')        #返回 'age' 属性的值
# setattr(emp, 'age', 8)      #添加属性 'age' 值为8
# delattr(emp, 'age')         #删除属性 'age'

# Python内置类属性
# __dict__:类的属性（包含一个字典，由类的数据属性组成）
# __doc__:类的文档字符串
# __name__:类名
# __module__:类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__等于mymod)
# __bases__:类的所有父类构成元素（包含了一个由所有父类组成的元组）

# Python内置类属性调用实例如下：
# class Employee:
#     '所有员工的基类'
#     empCount = 0
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
#
#     def displayEmployee(self):
#         print("Name:", self.name, ", Salary:", self.salary)
#
# print("Employee.__doc__:", Employee.__doc__)
# print("employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

# python对象销毁（垃圾回收）
# Python使用了引用计数这一简单技术来跟踪和回收垃圾。
# 在python内部记录着所有使用中的对象各有多少引用。
# 一个内部跟踪变量，称为一个引用计数器。
# 当对象被创建时，就创建了一个引用计数，当这个对象不再需要时，也就是说，这个对象的引用计数变为0时，它被垃圾回收。但是回收不是“立即”的，由解释器在适当的时机，将垃圾对象占用的内存空间回收。
# a = 40          #创建对象 <40>
# b = a           #增加引用， <40>的计数
# c = [b]         #增加引用. <40>的计数
#
# del a           #减少引用 <40> 的计数
# b = 100         #减少引用 <40> 的计数
# c[0] = -1       #减少引用 <40> 的计数

# 垃圾回收机制不仅针对引用计数为0的对象，同样也可以处理循环应用的情况。循环引用指的是，两个对象相互引用，但是没有其他变量引用他们。这种情况下，仅使用引用计数是不够的，Python的垃圾收集器实际上是一个引用计数器和一个循环垃圾收集器。作为引用计数的补存，垃圾收集器也会留心被分配的总量很大（即未通过引用计数销毁的那些）的对象。在这种情况下，解释器会暂停下来，试图清理所有未引用的循环。
# 实例
# 析构函数__del__, __del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行：
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print(class_name, "销毁")
#
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3))    #打印对象的id
# del pt1
# del pt2
# del pt3

# re.match函数
# re.match尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
# 函数语法：
# re.match(pattern, string, flags=0)

# import re
# print(re.match('www', 'www.runoob.com').span())     #在起始位置匹配
# print(re.match('com', 'www.runoob.com'))            #不在起始位置匹配

# import re
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if matchObj:
#     print("matchObj.group():", matchObj.group())
#     print("matchObj.group(1):", matchObj.group(1))
#     print("matchObj.group(2):", matchObj.group(2))
# else:
#     print("No match!!")

# re.search方法
# re.search扫描整个字符串并返回第一个成功的匹配。
# 函数语法：
# re.search(pattern, string, flags=0)

# import re
# print(re.search('www', 'www.runoob.com').span())        #在起始位置匹配
# print(re.search('com', 'www.runoob.com').span())        #不在起始位置匹配

# import re
#
# line = "Cats are smarter than dogs";
#
# searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)
#
# if searchObj:
#     print("searchObj.group():", searchObj.group())
#     print("searchObj.group(1): ", searchObj.group(1))
#     print("searchObj.group(2):", searchObj.group(2))
# else:
#     print("Nothing found!! ")

# re.match与re.search的区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match(r'dogs', line, re.M|re.I)
# if matchObj:
#     print("natch --> matchObj.group():", matchObj.group())
# else:
#     print("No match!!")
#
# matchObj = re.search(r'dogs', line, re.M|re.I)
# if matchObj:
#     print("search --> searchObj.group():", matchObj.group())
# else:
#     print("No match!!")

# 检索和替换
# Python的re模块提供了re.sub用于替换字符串中的匹配项。
# 语法：
# re.sub(pattern, repl, string, count=0, flags=0)

# 参数：
# pattern:正则中的模式字符串。
# repl：替换的字符串，也可为一个函数。
# string：要被查找替换的原始字符串。
# count：模式匹配后替换的最大次数，默认0表示替换所有的匹配。

# import re
#
# phone = "2004-959-559 # 这是一个国外电话号码"
#
# #删除字符串中的Python注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码是：", num)
#
# #删除非数字（-）的字符串
# num = re.sub(r'\D', "", phone)
# print("电话号码是：", num)

# repl参数是一个函数
# 以下实例中将字符串中的匹配的数字乘以2：
# import re
#
# #将匹配的数字乘以2
# def double(matched):
#     value = int(matched.group('value'))
#     return str(value * 2)
#
# s = 'A23G4HFD567'
# print(re.sub('(?P<value>\d+)', double, s))
# #?P<value>的意思就是命名一个名字为value的组，匹配规则符合后面的\d+（\d+匹配1个或更多连续的数字）

# re.compile函数
# compile函数用于编译正则表达式，生成一个正则表达式（Pattern）对象，供match()和search()这两个函数使用。
# 语法格式为：
# re.compile(pattern[, flags])

# 参数：
# pattern：一个字符串形式的正则表达式
# flags：可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
# 1、re.l 忽略大小写
# 2、re.L 表示特殊字符集\w,\W,\b,\B,\s,\S依赖于当前环境
# 3、re.M 多行模式
# 4、re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
# 5、re.U 表示特殊字符集\w,\W,\b.\B,\d,\D,\s,\S依赖于Unicode字符属性数据库
# 6、re.X 为了增加可读性，忽略空格和 # 后面的注释

# import re
# pattern = re.compile(r'\d+')                        #用于匹配至少一个数字
# m = pattern.match('one12twothree34four')            #查找头部，没有匹配
# print(m)
#
# m = pattern.match('one12twothree34four', 2, 10)     #从'e'的位置开始匹配，没有匹配
# print(m)
#
# m = pattern.match('one12twothree34four', 3, 10)     #从'1'的位置开始匹配，正好陪陪
# print(m)                                            #返回一个Match对象
#
# print(m.group(0))       #可忽略0
# print(m.start(0))       #可忽略0
# print(m.end(0))         #可忽略0
# print(m.span(0))        #可忽略0
# 在上面，当匹配成功是返回一个Match对象，其中：
# group([group1, ...])方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用group()或group(0);
# start([group])方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为0；
# end([group])方法用于获取分组匹配的子串在整个字符串中的结果位置（子串最后一个字符的索引+1），参数默认值为0；
# span([group])方法返回（start(group), end(group)）。

# import re
# line = "Cats are smarter than dogs"
#
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# if matchObj:
#     print("matchObj.group():", matchObj.group())
#     print("matchObj.group(1):", matchObj.group(1))
#     print("matchObj.group(2):", matchObj.group(2))
# else:
#     print("No match!!")

# import re
# s = '1102231990xxxxxxxx'
# res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})', s)
# print(res.groupdict())

