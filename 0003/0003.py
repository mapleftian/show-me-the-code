#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0003.py
   Author:        maple
   date:          2019/3/16 0:56
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0003题：
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中
'''

'''
思路：
先生成随机的优惠码，再逐个插入到Redis的List中
'''

'''
优化：
优化插入方式，补充插入时间等
'''
import redis
from randomCode import randomCodeList

#先生成激活码
RCode = randomCodeList()
codeNum = eval(input("输入需要获取的激活码的数量:\n"))
codeLenth = eval(input("输入激活码的长度:\n"))
codeList = RCode.getCodeList(codeNum,codeLenth)


#建立连接池
pool = redis.ConnectionPool(host = '127.0.0.1', port = 6379, password = '1231')
r = redis.Redis(connection_pool=pool)

#插入codeList
for code in codeList:
    r.rpush("codeList",code)

print("插入成功，总行数为%d"%(r.llen("codeList")))

#输出具体内容
num = r.llen("codeList")
for i in range(0,num):
    print(r.lindex("codeList",i).decode('utf8'))

print("\nEnd")