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

'''
思路：
读取excel中的文本信息
使用json.dump方式进行写入
'''

'''
优化：
使用dumps写入
'''

import json
import xlrd


def openXls():
    # 读取excel，读取sheet
    data = xlrd.open_workbook("student.xls")
    student = data.sheet_by_name("student")
    dict = {}
    list = []
    nor = student.nrows
    nol = student.ncols
    for x in range(0, nor):
        title = student.cell(x, 0)
        for y in range(1, nol):
            value = student.cell(x, y)
            list.append(value)
        dict[title] = list
        list = []
    return dict


if __name__ == '__main__':
    dict = openXls()
    print(dict)
