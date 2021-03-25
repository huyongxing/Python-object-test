#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/11 12:27
# @Author   : huyx
# @Site     : 
# @File     : radiobutton.py
# @Software : PyCharm

# 引入 CGI 处理模块
import cgi, cgitb

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
if form.getvalue('site'):
    site = form.getvalue('site')
else:
    site = "提交数据为空"

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI 测试实例</title>")
print("</head>")
print("<body>")
print("<h2> 选中的网址是 %s</h2>" % site)
print("</body>")
print("</html>")