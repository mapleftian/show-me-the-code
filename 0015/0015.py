#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0015.py
   Author:        Fynn-mac
   date:          2019-03-28 11:23
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0015题：
纯文本文件 city.txt为城市信息,
请将上述内容写到 city.xls 文件中，
'''

'''
思路：
1、读取文件
2、写入
'''

'''
优化：

'''
import json
import xlwt


# 读取文本内容
def readTxt():
    path = "city.txt"
    with open(path, 'r', encoding='utf-8') as f:  # 加入UTF-8，使得可以正常显示中文
        txt = json.loads(f.read())
    return txt


# 保存excel
def saveExcel():
    txt = readTxt()
    txt_key = txt.keys()
    new_excel = xlwt.Workbook(encoding='utf-8')
    new_sheet = new_excel.add_sheet('student')
    x = 0
    for key in txt_key:
        values = txt.get(key)
        new_sheet.write(x, 0, key)
        # print("key坐标({},{},)".format(x,0))
        # print(u"key is {} , value is {},坐标为({},{})".format(key,values,x,1))
        new_sheet.write(x, 1, label=values)
        x = x + 1
    new_excel.save('student.xls')


if __name__ == '__main__':
    saveExcel()
    print("end")