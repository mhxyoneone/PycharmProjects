# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban_movie.items import DoubanMovieItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    # rules = (
    #     Rule(LinkExtractor(allow=r'?start=\d+&filter="'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        # 第一层爬取所有分页页码加入集合
        # page1_url = []
        for i in range(0, 250, 25):
            url = 'https://movie.douban.com/top250?start={}'.format(i)
            # print(url)
            yield scrapy.Request(url=url, callback=self.parse_two)

    def parse_two(self, response):
        #爬取豆瓣250个页面详情页url
        douban_url = []
        urls = response.xpath('//div[@class="hd"]/a/@href').extract()
        for i in urls:
            # print('需要爬取的豆瓣url', i)
            yield scrapy.Request(url=i,callback=self.parse_third)

    def parse_third(self,response):
        #爬取数据
        print('开始爬取',response.url)
        # print('页面内容',response.content)
        items = DoubanMovieItem()
        items['movie_name'] = response.xpath('//h1/span/text()').extract()[0]
        items['rating_num'] = response.xpath('//div[@class="rating_self clearfix"]/strong/text()').extract()[0]
        items['movie_pic'] = response.xpath('//div[@id="mainpic"]/a/img/@src').extract()[0]
        # movie_director = response.xpath('//div[@id="info"]/span[1]').extract()
        # items['movie_actors'] =response.xpath('//div[@id="info"]/span[3]').extract()
        items['movie_type'] = self.movi_t(response)
        items['movie_introduction'] = self.movi_in(response)
        items['movie_director'] = self.movi_d(response)
        items['movie_actors'] = self.movi_a(response)
        yield items

    def movi_d(self,response):
        str = ''
        movie_director = response.xpath('//div[@id="info"]/span[1]/span[2]/a/text()').extract()
        movie_director = str.join(movie_director)
        return movie_director

    def movi_a(self,response):
        str = ''
        movie_actors = response.xpath('//div[@id="info"]/span[3]/span[2]//text()').extract()
        movie_actors = DoubanSpider.get_str(movie_actors)
        return movie_actors

    def movi_in(self,response):
        str = ''
        movie_introduction = response.xpath('//div[@id="link-report"]/span/text()').extract()
        movie_introduction = str.join(movie_introduction).replace('\n','').replace('\u2022','')
        return movie_introduction

    def movi_t(self,response):
        movie_type = response.xpath('//div[@id="info"]/span[@property="v:genre"]/text()').extract()
        movie_type = DoubanSpider.get_str(movie_type)
        return movie_type
    @classmethod
    def get_str(self,content):
        str = ''
        content = str.join(content)
        return content