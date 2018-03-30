# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class TiebaSpiderSpider(CrawlSpider):
    name = 'tieba_spider'
    allowed_domains = ['baidu.com']
    #start_urls = ['http://baidu.com/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'pn=/d+'), callback='parse_item', follow=True),
    # )

    def start_requests(self):
        name = input("请输入需要爬取的贴吧名：")
        url = "http://tieba.baidu.com/f?kw="+str(name)+"&ie=utf-8"  #http://tieba.baidu.com/f?kw=%E6%98%BE%E5%8D%A1&ie=utf-8&pn=50
        print("正在爬取"+ url)
        yield scrapy.Request(url=url,callback=self.parse_item)
    def parse_item(self, response):
        urls = []
        page = 0
        text = response.body
        #page = response.xpath('//a[@class="last pagination-item"]/@href').extract()
        rule = re.compile('pn=(\d+)" class="last pagination-item')
        num = rule.findall(str(text,encoding='utf-8'))[0]
        while page <= int(num):
            url = response.url + '&pn=' + str(page)
            urls.append(url)
            page += 50
        for i in urls:
            yield scrapy.Request(url=i,callback=self.parse_second)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()

    def parse_second(self,response):
        print('开始爬取帖子链接')
        rule = re.compile('href="(/p/\d+)')
        text_urls = rule.findall(str(response.body,encoding='utf-8'))
        #print(text_urls)
        for i in text_urls:
            text_url = 'https://tieba.baidu.com' + i
            yield scrapy.Request(url=text_url,callback=self.parse_third)

    def parse_third(self,response):
        print("开始爬取帖子内容")
        ids = response.xpath('//li[@class="d_name"]/a/text()').extract()
        send_times = response.xpath('//ul[@class="p_tail"]/li[2]/span/text()').extract()  #//div[@class="post-tail-wrap"]/span[4]/text()
        review_texts =response.xpath('//div[@class="d_post_content_main"]/div/cc/div/text()').extract()  #//div[@class="p_content  "]/cc/div/text()
        if len(send_times) > 0:
            send = send_times
            review = review_texts
        else:
            send = response.xpath('//div[@class="post-tail-wrap"]/span[4]/text()').extract()
            review = response.xpath('//div[@class="p_content  "]/cc/div/text()').extract()
        print(send,review,response.url)
        for id,send_time,review_text in zip(ids,send,review):
            data = {
                'id':id,
                'send_time':send_time,
                'review_text':review_text
            }
            print(data)

        #//li[@class="d_name"]/a/text()