# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from taonan.items import TaonanItem

class TaonanSpiderSpider(CrawlSpider):
    name = 'taonan_spider'
    allowed_domains = ['taonanw.com']
    start_urls = ['http://www.taonanw.com/?page=search_result_v2&search_type=search_quick&page_key=93e0a62a085397e93da5ed4bb727e0be&match_gender=1&match_r_state_id=6934&is_cut_img=1']

    rules = (
        Rule(LinkExtractor(allow=r'/p/\d+/search_type'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = TaonanItem()
        user_url = response.xpath('//div[@class="newsrchsult-act"]/a/@href').extract()
        for i in range(len(user_url)):
            items['user_url'] = 'http://www.taonanw.com'+ str(user_url[i])
            yield scrapy.Request(url=items['user_url'],callback=self.parse_second)

    def parse_second(self,response):
        items = TaonanItem()
        items['username'] = response.xpath('//div[@class="fl"]/a/h1/text()').extract()
        items['age'] = response.xpath('//span[@id="profile_age"]/text()').extract()
        items['header_pic'] =response.xpath('//div[@class="profile-user-img-box"]/a/img/@src').extract()
        items['image_pic']=response.xpath('//ul[@id="profile_photo"]//li/a/img/@src').extract()
        items['content'] = response.xpath('//span[@id="profile_about"]').extract()
        items['place_from'] = response.xpath('//span[@id="profile_n_state_id"]/@title').extract()
        items['education'] = response.xpath('//span[@id="profile_education"]/text()').extract()
        items['user_url']=response.url
        yield items