# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from PIL import Image
from io import BytesIO


class Tieba0013Pipeline(object):
    def process_item(self, item, spider):
        res = requests.get(item['imgUrl'])
        image = Image.open(BytesIO(res.content))
        path_save = "E:\coding\\爬虫内容\\贴吧图片\\"
        image.save(path_save + item['name'] + ".jpg")
        return item
