#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0004.py
   Author:        maple
   date:          2019/3/16 23:59
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0004题：
任一个英文的纯文本文件，统计其中的单词出现的个数
'''

'''
思路：
1、先剔除文本中所有的特殊符号,存在问题
2、使用split对文本内容进行分词并记录
3、输出单次出现的次数
'''

'''
优化：
1、增加词云等多功能展示形式
2、使用多线程进行分词
3、使用正则表达式对文本进行预处理
4、使用NLTK进行英文分词
5、符号的去除处理
'''

import wordcloud
import numpy as np
from PIL import Image
from nltk.corpus import stopwords

#清洗
txtUp = open('hamlet.txt').read()
txt = txtUp.lower()
for i in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~,\'':
    txt.replace(i," ")

#分词
codes = txt.split()
codeDic = {}
for code in codes:
    codeDic[code] = codeDic.get(code,0)+1

#去除无意义单次
sr = stopwords.words('english')
for key in list(codeDic.keys()):
    if key in sr:
        codeDic.pop(key)

#输出
items = list(codeDic.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(30):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

cloud_mask = np.array(Image.open('python.png'))

wc = wordcloud.WordCloud(
    background_color= 'white',
    font_path="C:/Windows/Fonts/Arial.ttf",  # 设置字体格式
    mask=cloud_mask,  # 设置背景图
    max_words=200,
    min_font_size=15,
    max_font_size=150,
    width=400
)

wc.generate_from_frequencies(codeDic)
wc.to_file("hamlet.png")



