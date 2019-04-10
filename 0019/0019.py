#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0019.py
   Author:        Fynn-mac
   date:          2019-04-10 17:00
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0019题：

'''

import xlrd
import xml.dom.minidom as mn

def read_xls():
    wb = xlrd.open_workbook('numbers.xls')
    ws = wb.sheet_by_index(0)
    data = []
    nro = ws.nrows
    for i in range(nro):
        values = ws.row_values(i)
        data.append(list(map(int,values)))
    return data

def write_xml(data):
    xmlfile = mn.Document()
    root = xmlfile.createElement('root')
    numbers = xmlfile.createElement('numbers')
    comments = xmlfile.createComment("数字信息")
    xmlcomments = xmlfile.createTextNode(str(data))
    xmlfile.appendChild(root)
    root.appendChild(numbers)
    numbers.appendChild(comments)
    numbers.appendChild(xmlcomments)
    #通过byte形式写入文件
    with open('number.xml','wb') as fp:
        fp.write(xmlfile.toprettyxml(encoding='UTF-8'))


if __name__ == '__main__':
    data = read_xls()
    write_xml(data)
    print('end')