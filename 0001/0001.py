#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0001.py
   Author:        maple
   date:          2019/3/13 21:26
   Software:      pycharm
-------------------------------------------------
"""

'''
第 0001 题：
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''

'''
思路：
1、产生随机大写字母函数
2、产生随机小写字母函数
3、产生随机数字函数
4、随机选择其中一种方式，连续随机codeLenth次
5、判断与之前产生是否重复，去重处理
6、重复，直至产生codeNum个激活码
'''

'''
优化：

'''

import random

def getStringRandom(codeLenth):
    code = ""
    for i in range(0,codeLenth):
        tmp = str(random.randint(1,3)) #此处需要对数字转化为字符，或者在IF中比较时，不加引号
        if tmp == '1':
            code = code + str(getRandomNum())
        elif tmp == '2':
            code = code + chr(getUpChar())
        else:
            code = code + chr(getLowerChar())
    return code

#随机数字
def getRandomNum():
    return random.randint(0,9)

#随机大写ASCII码
def getUpChar():
    return random.randint(0,25)+65

#随机小写ASCII码
def getLowerChar():
    return random.randint(0,25)+97

if __name__ == '__main__':
    codeNum = eval(input("输入需要获取的激活码的数量:\n"))
    codeLenth = eval(input("输入激活码的长度:\n"))
    i = 0
    codeList = []
    while i < codeNum :
        tmp = getStringRandom(codeLenth)
        if tmp not in codeList:
            codeList.append(tmp)
            i = i+1