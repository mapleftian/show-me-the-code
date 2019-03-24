#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0011.py
   Author:        Fynn-mac
   date:          2019-03-24 17:35
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0011题：
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights
'''

'''
思路：
1、先读取文本对单词，形成list列表
2、对用户输入对内容进行判断，如包含在内，就进行剔除处理
'''

'''
优化：

'''
def checkWord(str):
    list = readTxt()
    newStr= str
    for i in list:
        if i in str:
            newStr = "Freedom"
            break
        else:
            newStr = "Human Rights"
    print(newStr)

def readTxt():
    words = []
    with open("filtered_words.txt","r") as f:
        for word in f.readlines():
            words.append(word.strip())
    return words

if __name__ == '__main__':
    str = input("请输入内容：")
    checkWord(str)