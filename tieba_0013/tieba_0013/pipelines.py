# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
import os


class Tieba0013Pipeline(object):
    def process_item(self, item, spider):
        res = requests.get(item['imgUrl'])
        path = os.path.join(os.path.pardir,"Image")
        if not os.path.exists(path):
            os.mkdir(path)
        name = str(item['name']) + ".jpg"
        path_Image = os.path.join(path,name)
        with open(path_Image,'ab') as fp:
            fp.write(res.content)

        return item
