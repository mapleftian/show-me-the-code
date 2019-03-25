#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0012.py
   Author:        Fynn-mac
   date:          2019-03-24 19:15
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0012题：
敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

'''
思路：
1、读文件
2、对输入信息进行替换
3、replace函数的用法，是返回一个新的字符串，并不是直接对字符串进行操作。
'''

'''
优化：

'''

def checkWord(str):
    list = readTxt()
    replaceStr = str
    for i in list:
        if i in str:
            replaceStr = replaceStr.replace(i,"***")
    print(replaceStr)

def readTxt():
    words = []
    with open("filtered_words.txt",'r',encoding='UTF-8') as f:
        for word in f.readlines():
            words.append(word.strip())
    return words

if __name__ == '__main__':
    str = input("请输入内容：\n")
    checkWord(str)