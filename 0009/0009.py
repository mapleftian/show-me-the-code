#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0009.py
   Author:        Fynn-mac
   date:          2019-04-17 16:21
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0009题：
一个HTML文件，找出里面的链接
'''

'''
思路：
使用 来读取特定节点的href信息，获取连接
'''

'''
优化：
任意网页可以匹配出标准链接信息
'''
from bs4 import BeautifulSoup
import re
import requests


r = requests.get('https://www.hao123.com')
html_doc = ''
patter = re.compile('href = "(.*?)"')
href_list = re.findall(patter,r.text)
for href in href_list:
    print(href)

# soup = BeautifulSoup(html_doc,'lxml')
# tags = soup.find_all(name = '')
# for tag in tags:
#     print(tag['href'])