#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:     0010.py
   Author:        Fynn-mac
   date:          2019-03-19 22:49
   Software:      PyCharm
-------------------------------------------------
"""

'''
第0010题：
使用 Python 生成类似于下图中的字母验证码图片
'''

'''
思路：
1、创建空白画布
2、对画布内容进行调色处理
3、在画布上补充4个字符
4、模糊处理
'''

'''
优化：
1、通过内存生成图片
2、验证码提升复杂度


'''
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import sys

def randomChar():
    random_up = chr(random.randint(0,26)+65)
    random_lower = chr(random.randint(0,26)+97)
    random_num = str(random.randint(0,9))
    random_char = random.choice([random_up,random_lower,random_num])
    return random_char

def randomColor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def editImg():
    width = 60*4
    high = 60
    im = Image.new('RGB',(width,high),(255,255,255))
    draw = ImageDraw.Draw(im)
    if sys.platform == 'win32':
        font = ImageFont.truetype('C:/windows/fonts/Arial/arial.tff',size=30)
    else:
        font = ImageFont.truetype('/System/Library/Fonts/Arial.ttf',size=30)

    #背景多色处理
    # for x in range(width):
    #     for y in range(high):
    #         draw.point((x,y),fill=randomColor())

    #生成字符
    for i in range(4):
        draw.text((i*60+10,10),randomChar(),fill=randomColor(),font = font)

    #增加随机点
    for i in range(200):
        x = random.randint(0,width)
        y = random.randint(0,high)
        draw.point((x,y),fill=randomColor())

    #增加随机线
    for i in range(4):
        x1 = random.randint(0,width)
        y1 = random.randint(0,high)
        x2 = random.randint(0,width)
        y2 = random.randint(0,high)
        draw.line((x1,y1,x2,y2),fill=randomColor(),width=2)
    #在内存中生成图片
    # from io import BytesIO
    # f = BytesIO()
    # im.save(f,'jpeg')
    # data = f.getvalue()
    # f.close()
    # ff = open('checkCode.jpg','wb')
    # ff.write(data)


    #模糊效果
    #im = im.filter(ImageFilter.BLUR)

    im.save("checkCode.jpg",'jpeg')
    print("over")

if __name__ == '__main__':
    editImg()
    print("end")