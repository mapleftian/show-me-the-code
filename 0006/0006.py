#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0006.py
   Author:        Fynn-mac
   date:          2019-03-19 00:05
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0006题：
你有一个目录，放了你一个月的日记，都是txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词

'''

'''
思路：
扫描路径下对所有文档，
分别统计出出现频次最大对词
'''

'''
优化：
1、增加词云信息
2、对空文本的判断与处理
'''
import os
from nltk.corpus import stopwords

#判断用户所提供对路径是否存在
def dirNotExit(pathInput):
    if os.path.exists(pathInput):
        return False
    else:
        return True

#读取路径下对所有照片信息，并保存到一个列表中
def readTxt(pathInput):
    array_of_txt = []
    imgAll = os.walk(pathInput)
    for path,dirName,fileList in imgAll:
        for file in fileList:
            if file.endswith('txt') :
                array_of_txt.append(os.path.join(path,file))
            else:
                print("%s不是图片文件\n"%file)
    return array_of_txt

def maxWord(txtPath):
    txtUp = open(txtPath).read()
    txt = txtUp.lower()
    for i in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~,\'':
        txt.replace(i, " ")
    codes = txt.split()
    codeDic = {}
    for code in codes:
        codeDic[code] = codeDic.get(code, 0) + 1
    sr = stopwords.words('english')
    for key in list(codeDic.keys()):
        if key in sr:
            codeDic.pop(key)
    items = list(codeDic.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items[0]

if __name__ == '__main__':
    pathInput = input("请输入文件路径:\n")
    while dirNotExit(pathInput):
        pathInput = input("当前路径不存在，请重新输入:\n")
    array_of_txt = readTxt(pathInput)
    words = []
    for txt in array_of_txt:
        words.append(maxWord(txt))
