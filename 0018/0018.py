#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0018.py
   Author:        Fynn-mac
   date:          2019-04-10 14:31
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0018题：

'''

'''
思路：
1、读取excel中的内容
2、通过xml.dom.minidom生成xml文件

'''

'''
优化：

'''
import xlrd
import xml.dom.minidom as mn

def read_xls():
    path = 'city.xls'
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_index(0)
    nro = ws.nrows
    data = {}
    for i in range(nro):
        values = ws.row_values(i)
        data[values[0]] = values[1:]
    return data

def write_xml(data):
    xmlfile = mn.Document()

    root = xmlfile.createElement('root')
    city = xmlfile.createElement('city')
    comments = xmlfile.createComment(" 城市信息")
    xmlfile.appendChild(root)
    root.appendChild(city)
    city.appendChild(comments)
    xmlcomments = xmlfile.createTextNode(str(data))
    city.appendChild(xmlcomments)
    try:
        with open("city.xml",'w',encoding='UTF-8') as fp:
            xmlfile.writexml(fp,indent='',addindent='\t',newl='\n',encoding='UTF-8')
    except Exception as err:
        print('error{}'.format(err))

if __name__ == '__main__':
    data = read_xls()
    write_xml(data)
    print("end")
