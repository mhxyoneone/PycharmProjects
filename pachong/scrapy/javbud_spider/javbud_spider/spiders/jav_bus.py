# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from javbud_spider.items import JavbudSpiderItem

class JavBusSpider(CrawlSpider):
    name = 'jav_bus'
    allowed_domains = ['javbus.info']
    start_urls = ['https://www.javbus.info/']

    rules = (
        Rule(LinkExtractor(allow=r'/page/\d+')),
        Rule(LinkExtractor(allow=r'info/.*-\d+'),callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = JavbudSpiderItem()
        item = []
        item['movie_name'] = self.movie_name(response)[0]
        item['movie_id'] = self.movie_id(response)[0]
        item['movie_actor'] = self.movie_actor(response)
        item['movie_span'] = self.movie_span(response)
        item['movie_pic'] = self.movie_pic(response)[0]
        yield scrapy.request()

    def movie_name(self,response):
        name = response.xpath('//div[@class="container"]/h3/text()').extract()
        if len(name) > 0:
            movie_name = name
        else:
            movie_name = "Null"
        return movie_name

    def movie_actor(self,response):
        actor = response.xpath('//div[@class="col-md-3 info"]/p[10]/span/a/text()').extract()
        if len(actor) > 0:
            movie_actor = actor
        else:
            movie_actor = "Null"
        return movie_actor

    def movie_id(self,response):
        id = response.xpath('//div[@class="col-md-3 info"]/p[1]/span[2]/text()').extract()
        if len(id) > 0:
            movie_id = id
        else:
            movie_id = "Null"
        return movie_id

    def movie_span(self,response):
        span = response.xpath('//div[@class="col-md-3 info"]/p[8]/span/a/text()').extract()
        span1 = ","
        if len(span) > 0:
            movie_span = span1.join(span)
        else:
            movie_span = "Null"
        return movie_span

    def movie_pic(self,response):
        pic = response.xpath('//a[@class="bigImage"]/img/@src').extract()
        if len(pic) > 0 :
            movie_pic = pic
        else:
            movie_pic = "Null"
        return movie_pic