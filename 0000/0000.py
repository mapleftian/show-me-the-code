#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
-------------------------------------------------
   File Name:     0000.py
   Author:        maple
   date:          2019-03-13 18:03
   Software:      pycharm
-------------------------------------------------
"""

'''
第 0000 题：
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
'''

'''
思路：
PIL中Image类可以读取图片，并对图片内容进行修改。
'''

###########
'''
优化：
1、比如对任意一张图片进行图片规整，之后对任意长度对数据均能正常显示在图片上
2、可以判断图片对色彩，自动选择匹配对文字颜色
'''

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open("down.jpeg")
draw = ImageDraw.Draw(img)
fontStyle = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",150,encoding="unic")
width,height = img.size
draw.text((width/1.3,20),"100",fill=(255,0,0),font=fontStyle)
img.save("new.jpg")
