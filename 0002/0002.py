#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0002.py
   Author:        maple
   date:          2019/3/14 22:27
   Software:      pycharm
-------------------------------------------------
"""

'''
第0002题：
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
'''

'''
思路：
1、先使用随机数对象生成随机码
2、建立mysql驱动
3、批量执行插入SQL
4、统一执行
'''

'''
优化：
插入前对表是否存在进行判断，若存在，就插入数据，若不存在，就先创建表

'''

import pymysql
from randomCode import randomCodeList

#先生成激活码
RCode = randomCodeList()
codeNum = eval(input("输入需要获取的激活码的数量:\n"))
codeLenth = eval(input("输入激活码的长度:\n"))
codeList = RCode.getCodeList(codeNum,codeLenth)

#连接数据库
conn = pymysql.Connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '1231',
    db = 'self_ind',
    charset = 'utf8'
)

cursor = conn.cursor()


for code in codeList:
    sql = "INSERT into codelist (" \
          "codes,used)" \
          "VALUES (%s,%s)"
    a=cursor.execute(sql,(code,1))
    print("a="+str(a))

try:
    conn.commit()
except:
    conn.rollback()

conn.close()

print("end")