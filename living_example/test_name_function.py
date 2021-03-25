#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:    : 2021/3/22 11:41
# @Author   : huyx
# @Site     : 
# @File     : test_name_function.py
# @Software : PyCharm

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# unittest.main()
# 创建的.py文件名不能以test方法开头，需要去掉“main()”后面的括号，如下：
# unittest.main
# 或者将unittest.main()换成如下方法：
# if __name__ == '__main__':
#     get_formatted_name
# 或者将unittest.main()换成如下方法：
if __name__ == '__main__':
    unittest.main()
