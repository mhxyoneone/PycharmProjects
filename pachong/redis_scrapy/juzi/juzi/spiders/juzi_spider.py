# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from juzi.items import JuziItem
from scrapy_redis.spiders import RedisCrawlSpider

class JuziSpiderSpider(RedisCrawlSpider):
    name = 'juzi_spider'
    #allowed_domains = ['itjuzi.com']
    redis_key = 'juzi:start_urls'
    # start_urls = [
    #     'http://www.itjuzi.com/company?page=1/'
    # ]
    rules = (
        Rule(link_extractor=LinkExtractor(allow=('/company\?page=\d+'))),
        Rule(link_extractor=LinkExtractor(allow=('/company/foreign\?page=\d+'))),
        # 获取每一个公司的详情
        Rule(link_extractor=LinkExtractor(allow=('/company/\d+')), callback='parse_item')
    )
    headers = {
        "Host": "www.itjuzi.com",
        "Connection": "keep-alive",
        # "Upgrade-Insecure-Requests" : "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        # "Referer" : "http://www.itjuzi.com/company",
        "Cookie": "gr_user_id=b609a4a5-8b03-4078-85b5-0bb0e617daf5; _hp2_id.2147584538=%7B%22userId%22%3A%225361264262655533%22%2C%22pageviewId%22%3A%222812157498870176%22%2C%22sessionId%22%3A%221376560908636027%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; identity=123636274%40qq.com; remember_code=3zB55lODqf; acw_tc=AQAAAMOWGBUfUwgAU3Awtjx04lI+Gr0e; acw_sc=589c0d25fa257c17aedfa3127a7c3a0eac145db7; session=4f1aec94fd99840a562f39488480a9b2798824f9; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1486565620,1486575689,1486603765,1486603844; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1486624109; ",
        "If-Modified-Since": "Thu, 08 Feb 2018 04:34:46 GMT",
        "Cache - Control": "max - age = 0"

    }
    #处理cookie
    def make_requests_from_url(self, url):
        return scrapy.Request(url,
                headers = self.headers,
                dont_filter = True)
    #动态域
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(JuziSpiderSpider, self).__init__(*args, **kwargs)
    #爬取主体
    def parse_item(self, response):
        items = JuziItem()
        #items['company_name'] = response
        items['company_name'] = self.company_name(response)
        items['company_id'] = self.company_id(response)
        items['slogan'] = self.slogan(response)
        items['scope'] = self.scope(response)
        items['home_page'] = self.home_page(response)
        items['tags'] = self.tags(response)
        items['company__full_name'] = self.company_full_name(response)
        items['company__info'] = self.company_info(response)
        items['found_time'] = self.found_time(response)
        items['company__size'] = self.company_size(response)
        items['company__status'] = self.company_status(response)
        items['tz_info'] = self.tz_info(response)
        items['team_info'] = self.team_info(response)
        items['pro_info'] = self.pro_info(response)
        yield items


    #公司名字
    def company_name(self,response):
        resp = response.xpath('//div[@class="line-title"]/span[@class="title"]/h1/text()').extract()
        if len(resp) != 0:
            name = resp[0]
        else:
            name = "Null"
        return name
    #公司编号
    def company_id(self,response):
        id = response.url.spilt('/')[-1]
        return id
    #公司口号
    def slogan(self,response):
        logan = response.xpath('//h2[@class="seo-slogan"]/text()').extract()
        if len(logan) != 0:
            return logan[0]
        else:
            return 'Null'
    #公司分类
    def scope(self, response):
        sc = response.xpath('//span[@class="scope c-gray-aset"]/text()').extract()
        if len(sc) != 0:
            return sc[0]
        else:
            return 'Null'

    #公司主页
    def home_page(self, response):
        hp = response.xpath('//div[@class="link-line"]/a[3]/@href').extract()
        if len(hp) != 0:
            return hp[0]
        else:
            return 'Null'
    #公司标签
    def tags(self, response):
        tag = response.xpath('//div[@class="tagset dbi c-gray-aset tag-list"]/a/text()').extract()
        if len(tag) != 0:
            return tag
        else:
            return 'Null'

    #公司全称
    def company_full_name(self, response):
        cfn = response.xpath('//h2[@class="seo-second-title margin-right50"]/text()').extract()
        if len(cfn) != 0:
            return cfn[0]
        else:
            return 'Null'
    #公司信息
    def company_info(self, response):
        info = ","
        comin = response.xpath('//div[@class="block"]/div[2]/text()').extract()
        if len(comin) != 0:
            info = info.join(comin).strip()
            return info
        else:
            return 'Null'
    #创建时间
    def found_time(self, response):
        fout = response.xpath('//div[@class="des-more"]/h3[1]/span/text()').extract()
        if len(fout) != 0:
            return fout[0]
        else:
            return 'Null'
    #公司规模
    def company_size(self, response):
        cs = response.xpath('//div[@class="des-more"]/h3[2]/span/text()').extract()
        if len(cs) != 0:
            return cs[0]
        else:
            return 'Null'
    #运营状态
    def company_status(self, response):
        css = response.xpath('//div[@class="des-more"]/span/text()').extract()
        if len(css) != 0:
            return css
        else:
            return 'Null'
    #投资情况
    def tz_info(self, response):
        tz=[]
        tz_in_a = response.xpath('//tr[@class="feedback-btn-parent"]/td[1]').extract()
        tz_in_b = response.xpath('//tr[@class="feedback-btn-parent"]/td[2]').extract()
        tz_in_c = response.xpath('//tr[@class="feedback-btn-parent"]/td[3]').extract()
        tz_in_d = response.xpath('//tr[@class="feedback-btn-parent"]/td[4]').extract()
        if len(tz_in_a) != 0:
            tz.append(tz_in_a.strip())
            tz.append(tz_in_b.strip())
            tz.append(tz_in_c.strip())
            tz.append(tz_in_d.strip())
            return tz
        else:
            return 'Null'
    #团队情况
    def team_info(self, response):
        infomation = []
        for i in response.xpath('//li[@class="feedback-btn-parent first-letter-box-4js"]'):
            name = i.xpath('./div[1]/a/text()').extract()
            positon = i.xpath('./div[2]/text()').extract()
            info = i.xpath('./div[3]/div/text()').extract().strip()
            infomation.append(name and positon and info)
        return infomation

    # 产品信息
    def pro_info(self,response):
        return 'Null'

