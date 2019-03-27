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
2、使用xlwt写入并生成xls文件
'''

'''
优化：
使用xlsxwriter生成xlsx文件
'''
import json
import xlwt


# 读取文本内容
def readTxt():
    path = "student.txt"
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
        # print("key坐标({},{})".format(x,0))
        for y in range(len(values)):
            # print(u"key is {} , value is {},坐标为({},{})".format(key,values[y],x,y+1))
            new_sheet.write(x, y + 1, label=values[y])
        x = x + 1
    new_excel.save('student.xls')


if __name__ == '__main__':
    saveExcel()
