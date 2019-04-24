# -*- coding: utf-8 -*-
import scrapy
from tieba_0013.items import Tieba0013Item


class TiebaspiderSpider(scrapy.Spider):
    name = 'tiebaSpider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/p/2166231880/']

    def parse(self, response):
        subSelector = response.xpath('//*[@id="j_p_postlist"]/div/div[3]/div[1]')
        items = []
        count = 1
        for sub in subSelector:
            item = Tieba0013Item()
            sub_url = sub.xpath('//img/@src').extract()
            for i in range(len(sub_url)):
                item['imgUrl'] = sub.xpath('//img/@src').extract()[i]
                item['name'] = count
                items.append(item)
                count = count + 1
        return items
