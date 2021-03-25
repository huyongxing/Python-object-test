#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/9 13:53
# @Author   : huyx
# @Site     : 
# @File     : cgi_variate.py
# @Software : PyCharm

import os

print("Content-type: text/html")
print()
print("<mata charset=\"utf-8\">")
print("<b>环境变量</b><br>");
print("<ul>")
for key in os.environ.keys():
    print("<li><span style='color:green'>%30s </span> : %s </li>" % (key,os.environ[key]))
print("</ul>")