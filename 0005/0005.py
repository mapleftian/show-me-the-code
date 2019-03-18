#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0005.py
   Author:        fynn
   date:          2019-03-18 16:36
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0005题：
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
'''

'''
思路：
1、先输入文件路径，扫描路径下存在对所有文件，找到所有对图片类型文件
2、对图片宽和高进行判断，
'''

'''
优化：
1、找出指定某个文件夹及其子文件夹下的图片
'''
'''
知识点：
os.listdir只能找到该路径下对文件，对该路径下对文件夹无用
再通过filename.endwith来判断是否是jpg/png格式
os.walk()将生成迭代器，包含路径path，文件夹名dirName，文件名fileName

'''

import os
from PIL import Image

#判断用户所提供对路径是否存在
def dirNotExit(pathInput):
    if os.path.exists(pathInput):
        return False
    else:
        return True

#读取路径下对所有照片信息，并保存到一个列表中
def readImage(pathInput):
    array_of_img = []
    imgAll = os.walk(pathInput)
    for path,dirName,fileList in imgAll:
        for file in fileList:
            if file.endswith('png') :
                array_of_img.append(os.path.join(path,file))
            elif file.endswith('jpeg'):
                array_of_img.append(os.path.join(path,file))
            elif file.endswith('jpg') :
                array_of_img.append(os.path.join(path,file))
            else:
                print("%s不是图片文件\n"%file)
    return array_of_img

#创造新的文件夹路径，用于保存处理后对图片
def mkNewDir(newPath):
    if os.path.exists(newPath):
        print("文件夹已经存在")
    else:
        os.mkdir(newPath)

#编辑图片
#进行等比例缩减
#iPhone5分辨率为：1136*640
def editImage(i,newPath,counter):
    iPhone5_w = 1136
    iPhone5_h = 640
    fileName = os.path.basename(i)
    im = Image.open(i)
    w,h = im.size

    if w/h == iPhone5_w/iPhone5_h:
        im.resize((iPhone5_w, iPhone5_h), Image.ANTIALIAS)

    if w > iPhone5_w :
        h_new=iPhone5_w*h/w
        w_new=iPhone5_w
        im.resize((w_new,h_new),Image.ANTIALIAS)

    if h > iPhone5_h:
        w_new=iPhone5_h*w/h
        h_new=iPhone5_h
        im.resize((w_new,h_new),Image.ANTIALIAS)

    if os.path.exists(os.path.join(newPath,fileName)):
        fileName = str(counter)+"--"+fileName
    im.save(os.path.join(newPath,fileName))



if __name__ == '__main__':
    pathInput = input("请输入图片路径:\n")
    while dirNotExit(pathInput):
        pathInput = input("当前路径不存在，请重新输入:\n")
    array_of_img = readImage(pathInput)
    newPath = os.path.join(pathInput,'newImages_iPhone5')
    mkNewDir(newPath)
    counter = 0
    for i in array_of_img:
        editImage(i,newPath,counter)
        counter = counter +1
    print("end")
