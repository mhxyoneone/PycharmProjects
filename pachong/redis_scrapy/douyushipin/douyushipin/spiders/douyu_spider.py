# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import json
import re
import string
from douyushipin.items import DouyushipinItem

class DouyuSpiderSpider(scrapy.Spider):
    name = 'douyu_spider'
    allowed_domains = ['douyu.com']
    #start_urls = ['https://www.douyu.com/directory/all']
    url = "https://www.douyu.com/gapi/rkc/directory/0_0/"
    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )
    # def page_num(self):
    #     num = int(input("请输入需要爬取的页数:"))
    #     return num
    def start_requests(self):
        num = int(input("请输入需要爬取的页数:"))
        for i in range(1,num+1) :
            url = self.url + str(i)
            print("开始爬取第"+str(i)+"页")
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # js =  string.replace()
        resp = response.body
        rule = re.compile(r'"url":"/(.*?)"')
        urls = rule.findall(str(resp))
        for i in urls:
            url = 'https://www.douyu.com/'+ i
            yield scrapy.Request(url=url,callback=self.parse_two)
            #print(url)
    def parse_two(self,response):
        items = DouyushipinItem()
        items['hot'] = response.xpath('//div[@class="headline clearfix"]/h2/text()').extract()
        yield items

