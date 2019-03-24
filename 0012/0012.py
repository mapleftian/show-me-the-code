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

'''

'''
思路：

'''

'''
优化：

'''

def checkWord(str):
    list = readTxt()
    newStr= str
    replaceStr = str
    for i in list:
        if i in str:
            newStr = "Freedom"
            print(i)
            replaceStr.replace("北京","**")
            break
        else:
            newStr = "Human Rights"
    print(newStr)
    print(replaceStr)

def readTxt():
    words = []
    with open("filtered_words.txt","r") as f:
        for word in f.readlines():
            words.append(word.strip())
    return words

if __name__ == '__main__':
    str = input("请输入内容：")
    checkWord(str)