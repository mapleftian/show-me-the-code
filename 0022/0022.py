#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0022.py
   Author:        fynn-PC
   date:          2019/4/10 22:46
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0022题：

'''

'''
思路：

'''

'''
优化：

'''

import os
from PIL import Image


def dirNotExit(self, pathInput):
    if os.path.exists(pathInput):
        return False
    else:
        return True


class editImages(object):
    def __init__(self, iPhone_w, iPhone_h):
        self.iPhone_w = iPhone_w
        self.iPhone_h = iPhone_h

    # 读取路径下对所有照片信息，并保存到一个列表中
    def readImage(self, pathInput):
        array_of_img = []
        imgAll = os.walk(pathInput)
        for path, dirName, fileList in imgAll:
            for file in fileList:
                if file.endswith('png'):
                    array_of_img.append(os.path.join(path, file))
                elif file.endswith('jpeg'):
                    array_of_img.append(os.path.join(path, file))
                elif file.endswith('jpg'):
                    array_of_img.append(os.path.join(path, file))
                else:
                    print("%s不是图片文件\n" % file)
        return array_of_img

    def editImage(self, i, newPath, counter):
        fileName = os.path.basename(i)
        im = Image.open(i)
        w, h = im.size

        if w / h == self.iPhone_w / self.iPhone_h:
            im.resize((self.iPhone_w, self.iPhone_h), Image.ANTIALIAS)

        if w > self.iPhone_w:
            h_new = self.iPhone_w * h / w
            w_new = self.iPhone_w
            im.resize((w_new, h_new), Image.ANTIALIAS)

        if h > self.iPhone_h:
            w_new = self.iPhone_h * w / h
            h_new = self.iPhone_h
            im.resize((w_new, h_new), Image.ANTIALIAS)

        if os.path.exists(os.path.join(newPath, fileName)):
            fileName = str(counter) + "--" + fileName
        im.save(os.path.join(newPath, fileName))

    # 创造新的文件夹路径，用于保存处理后对图片
    def mkNewDir(newPath):
        if os.path.exists(newPath):
            print("文件夹已经存在")
        else:
            os.mkdir(newPath)


if __name__ == '__main__':
    iPhone_dict = {'iPhone5s': {'w': 640, 'h': 1136}, 'iPhone6': {'w': 750, 'h': 1134},
                   'iPhone6sPlus': {'w': 1242, 'h': 2208}}
    pathInput = input("请输入图片路径:\n")
    while dirNotExit(pathInput):
        pathInput = input("当前路径不存在，请重新输入:\n")
    iPhone_type = input("请输入iPhone型号：\n")
    im = editImages(iPhone_dict[iPhone_type]['w'], iPhone_dict[iPhone_type]['h'])
    array_of_img = im.readImage(pathInput)
    newPath = os.path.join(pathInput, 'newImages_iPhone5')
    im.mkNewDir(newPath)
    counter = 0
    for i in array_of_img:
        im.editImage(i, newPath, counter)
        counter = counter + 1
    print("end")
