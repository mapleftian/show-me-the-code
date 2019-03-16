#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     randomCode.py
   Author:        maple
   date:          2019/3/15 23:09
   Software:      PyCharm
-------------------------------------------------
"""


import random

#随机产生激活码的类
class randomCodeList(object):

    #初始化
    def __init__(self):
        pass

    def getCodeList(self,num,lenth):
        codeNum = num
        codeLenth = lenth
        i = 0
        codeList = []
        while i < codeNum:
            tmp = self.getStringRandom(codeLenth)
            if tmp not in codeList:
                codeList.append(tmp)
                i = i + 1
        return codeList


    #返回一个激活码
    def getStringRandom(self,codeLenth):
        code = ""
        for i in range(0, codeLenth):
            tmp = str(random.randint(1, 3))
            if tmp == '1':
                code = code + str(self.getRandomNum())
            elif tmp == '2':
                code = code + chr(self.getUpChar())
            else:
                code = code + chr(self.getLowerChar())

        return code

    # 随机数字
    def getRandomNum(self):
        return random.randint(0, 9)

    # 随机大写ASCII码
    def getUpChar(self):
        return random.randint(0, 25) + 65

    # 随机小写ASCII码
    def getLowerChar(self):
        return random.randint(0, 25) + 97
