#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0014.py
   Author:        Fynn-mac
   date:          2019-03-27 16:22
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0014题：
纯文本文件 student.txt为学生信息, 
请将上述内容写到 student.xls 文件中
'''

'''
思路：
1、使用Json读取txt格式对内容，生成字典类型
2、
'''

'''
优化：

'''
import json

#读取文本内容
def readTxt():
    path = "student.txt"
    with open(path,'r') as f:
        txt = json.loads(f.read())
    return txt

def saveExcel():
    txt= readTxt()
    txt_key = txt.keys()
    x = 0
    y = 0
    for key in txt_key:
        values = txt.get(key)
        y = 0
        for value in range(len(values)):
            print("key is {} , value is {},坐标为({},{})".format(key,values[value],x,y))
            y = y + 1
        x = x + 1

if __name__ == '__main__':
    saveExcel()
