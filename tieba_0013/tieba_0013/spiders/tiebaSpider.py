# -*- coding: utf-8 -*-
import scrapy
from tieba_0013.items import Tieba0013Item
import re


class TiebaspiderSpider(scrapy.Spider):
    name = 'tiebaSpider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/p/2166231880']

    def parse(self, response):
        subSelector = response.xpath('//*[@id="j_p_postlist"]/div/div[3]/div[1]')
        items = []
        count = 0
        for i in range(len(subSelector)):
            content = subSelector[i].extract()
            pa = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
            url_list = re.findall(pa, content)
            for url in url_list:
                item = Tieba0013Item()
                item['imgUrl'] = url
                item['name'] = count
                count = count + 1
                items.append(item)
        return items
