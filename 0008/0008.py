#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0008.py
   Author:        Fynn-mac
   date:          2019-04-17 16:20
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0008题：
一个HTML文件，找出里面的正文
'''

'''
思路：
通过正则选择所有的键值对中间的值，前提是没有添加css内容
有css内容的需要再优化，或者再定向的选择内容
'''

'''
优化：

'''

import re

html_doc = ''
patter = re.compile('<.*?>(.*?)<.*?>')
text_list = []
text_list = re.findall(patter,html_doc)
#去掉内容为空格的
text = [item for item in text_list if item.strip()]
print(text)