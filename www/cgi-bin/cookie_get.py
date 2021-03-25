#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/11 16:14
# @Author   : huyx
# @Site     : 
# @File     : cookie_get.py
# @Software : PyCharm

# 导入模块
import os
import http.cookies

print("Content-type: text/html")
print()

print("""
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h1>读取cookie信息</h1>
""")

if 'HTTP_COOKIE' in os.environ:
    cookie_string=os.environ.get('HTTP_COOKIE')
    c=http.cookies.SimpleCookie()
    # c=Cookie.SimpleCookie()
    c.load(cookie_string)

    try:
        data=c['name'].value
        print("cookie data: "+data+"<br>")
    except KeyError:
        print("cookie 没有设置或者已过期<br>")
print("""
</body>
</html>
""")