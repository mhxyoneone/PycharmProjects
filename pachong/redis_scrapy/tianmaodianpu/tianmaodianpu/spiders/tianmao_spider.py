# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TianmaoSpiderSpider(CrawlSpider):
    name = 'tianmao_spider'
    allowed_domains = ['tmall.com']
    start_urls = ['https://pg.tmall.com//pg.tmall.com/search.htm?search=y']

    rules = (
        Rule(LinkExtractor(allow=r'pageNo=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response.body)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

