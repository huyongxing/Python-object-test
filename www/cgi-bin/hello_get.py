#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/9 13:49
# @Author   : huyx
# @Site     : 
# @File     : hello_get.py
# @Software : PyCharm

# CGI处理模块
import cgi, cgitb

# 创建 FieldStorage的实例化
form = cgi.FieldStorage()

# 获取数据
site_name = form.getvalue('name')
site_url = form.getvalue('url')

print("Content-type:text/html")
print()
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>菜鸟教程 CGI测试实例</title>")
print("</head>")
print("<body>")
print("<h2>%s官网：%s</h2>" % (site_name, site_url))
print("</body>")
print("</html>")