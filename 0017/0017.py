#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0017.py
   Author:        fynn-PC
   date:          2019/4/1 22:39
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0017题：
将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
'''

import xlrd
from xml.etree.ElementTree import Element, SubElement, Comment, ElementTree
import xml.dom.minidom as md

def openXls():
    # 读取excel，读取sheet
    data = xlrd.open_workbook("student.xls")
    student = data.sheet_by_name("student")
    dict = {}
    nor = student.nrows
    for x in range(nor):
        dict[x + 1] = student.row_values(x)[1:]
    return dict


def write_to_xml(xlscontent):
    # 创建新xml文件
    xmlfile = md.Document()

    # 创建节点
    root = xmlfile.createElement('root')
    # 创建节点
    students = xmlfile.createElement('students')
    # 在文件中添加root节点
    xmlfile.appendChild(root)
    # 在root下添加students节点
    root.appendChild(students)
    # 创建评论
    comment = xmlfile.createComment('学生信息表 "id" : [名字, 数学, 语文, 英文]')
    # 在students标签下添加comment
    students.appendChild(comment)
    # 创建文本节点
    xmlcontent = xmlfile.createTextNode(str(xlscontent))
    # 在students标签下添加文本内容
    students.appendChild(xmlcontent)
    # 写入文件
    with open('students.xml', 'wb') as f:
        f.write(xmlfile.toprettyxml(encoding='utf-8'))


def write_to_xml_2(data):
    root = Element('root')
    comment = Comment('学生信息表"id" : [名字, 数学, 语文, 英文]')
    root.append(comment)
    child = SubElement(root, 'students')
    child.text = str(data)
    tree = ElementTree(root)
    tree.write('student2.xml', encoding='utf8')

if __name__ == '__main__':
    data = openXls()
    print(data)
    write_to_xml(data)
    write_to_xml_2(data)
