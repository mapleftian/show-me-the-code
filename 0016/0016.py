#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0016.py
   Author:        Fynn-mac
   date:          2019-03-29 17:47
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0016题：
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示
请将上述内容写到 numbers.xls 文件中
'''

'''
思路：
与之前一致
'''

'''
优化：

'''
import json
import xlwt

def readTxt():
    path = "numbers.txt"
    with open(path,'r',encoding='utf-8') as f :
        lists = json.loads(f.read())
    return lists

def saveExcel():
    new_excel = xlwt.Workbook(encoding='utf-8')
    sheet = new_excel.add_sheet('numbers')
    lists = readTxt()
    for x in range(len(lists)):
        for y in range(len(lists[x])):
            sheet.write(x,y,label = lists[x][y])
    new_excel.save("numbers.xls")

if __name__ == '__main__':
    saveExcel()
    print("end")
