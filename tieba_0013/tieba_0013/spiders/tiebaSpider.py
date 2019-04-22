# -*- coding: utf-8 -*-
import scrapy
from tieba_0013.item import Tieba0013Item


class TiebaspiderSpider(scrapy.Spider):
    name = 'tiebaSpider'
    allowed_domains = ['http://tieba.baidu.com/p/2166231880']
    start_urls = ['http://http://tieba.baidu.com/p/2166231880/']

    def parse(self, response):
        subSelector = response.xpath('//*[@id="j_p_postlist"]/div/div[3]/div[1]')
        items = []
        count = 1
        for sub in subSelector:
            item = Tieba0013Item()
            item['imgUrl'] = sub.xpath('//img/@src').extract()[0]
            item['name'] = count
            items.append(item)
            count = count + 1
        return items
