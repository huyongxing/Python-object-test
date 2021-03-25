#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/11 17:51
# @Author   : huyx
# @Site     : 
# @File     : save_file.py
# @Software : PyCharm

import cgi, os
import cgitb;

cgitb.enable()

form = cgi.FieldStorage()

# 获取文件名
fileitem = form['filename']

# 检测文件是否上传
if fileitem.filename:
    # 设置文件路径 linux
    # fn = os.path.basename(fileitem.filename)
    # open('/tmp/' + fn, 'wb').write(fileitem.file.read())
    # 设置文件路径 windows
    fn = os.path.basename(fileitem.filename.replace("\\", "/" ))

    message = '文件 "' + fn + '" 上传成功'

else:
    message = '文件没有上传'

print("""\
Content-Type: text/html\n
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))