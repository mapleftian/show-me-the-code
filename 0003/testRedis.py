#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     testRedis.py
   Author:        maple
   date:          2019/3/16 22:34
   Software:      PyCharm
-------------------------------------------------
"""
import redis

#建立连接池
#当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中，当程序需要进行数据库访问时，
#无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
pool = redis.ConnectionPool(host = '127.0.0.1',port = 6379,password = '1231')
r = redis.Redis(connection_pool=pool)

#查
print (r.get("mykey").decode('utf8'))

#增加List 右侧增加
r.rpush("list2", 44, 55, 66)
print(r.llen("list2"))