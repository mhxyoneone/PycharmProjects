# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from javbud_spider.items import JavbudSpiderItem
import re
from scrapy_redis.spiders import RedisCrawlSpider
import requests

class JavBusSpider(CrawlSpider):
    name = 'jav_bus'
    allowed_domains = ['javbus.info']
    start_urls = ['##############']
    #redis_key = "jav:start_url"

    rules = (
        Rule(LinkExtractor(allow=r'/page/\d+')),
        Rule(LinkExtractor(allow=r'info/.*-\d+'),callback='parse_item', follow=True),
    )

    headers = {
        'authority': '#######',
        'method': 'GET',
        'path': '/ajax/uncledatoolsbyajax.php?gid=36417994212&lang=zh&img=https://pics.javcdn.pw/cover/6f58_b.jpg&uc=0&floor=280',
        'scheme': 'https',
        'accept': '*/*',
        # 'accept-encoding':'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__cfduid=dbc14b3bc854c776636d1035548a5f54e1516261025; HstCfa3288802=1516261062336; HstCmu3288802=1516261062336; __dtsu=2DE7B66BC84E605AC20C3E85029CA511; PHPSESSID=4jvt428b36d9jjd4npc5vism55; HstCla3288802=1518094188397; HstPn3288802=1; HstPt3288802=19; HstCnv3288802=4; HstCns3288802=6',
        'referer': 'https://www.javbus.info/BSTC-017',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(JavBusSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = JavbudSpiderItem()
        print("一层爬取")
        #items = []
        item['movie_name'] = self.movie_name(response)[0]
        item['movie_id'] = self.movie_id(response)[0]
        item['movie_actor'] = self.movie_actor(response)
        item['movie_span'] = self.movie_span(response)
        item['movie_pic'] = self.movie_pic(response)[0]
        movie_pid_url = self.movie_pid_url(response)
        item['movie_torrent'] = self.parse_second(movie_pid_url)
        #items.append(item)
        #for item in items:
        #print("return")
            #yield scrapy.Request(item['movie_pid_url'],meta={"meta_1":item},callback=self.parse_second,dont_filter=True)
        yield item
        print("爬取完成")

        #item['movie_torrent'] = response.extract()
        #yield item

    def parse_second(self,url):
        # print("开始二层爬取")
        # items  = JavbudSpiderItem()
        # item = response.meta['meta_1']
        # items['movie_torrent'] = self.movie_torrent(response)
        # items['movie_name'] = item['movie_name'][0]
        # items['movie_id'] = item['movie_id'][0]
        # items['movie_actor'] = item['movie_actor']
        # items['movie_span'] = item['movie_span']
        # items['movie_pic'] = item['movie_pic'][0]
        # items['movie_pid_url'] = response.url
        # #items['sdad'] = response.xpath('dsad').extract
        print('第二层爬取')
        response = requests.get(url, headers=self.headers)
        response1 = response.text
        # movie_torrent = response.body.decode('utf-8')
        torrent = re.compile(r'href="(.*?)"')
        magent = ",".join(torrent.findall(response1))
        return magent
        #yield items



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
            movie_actor = ','.join(actor)
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
    def movie_pid_url(self,response):
        pid = response.xpath('/html/body/script[3]/text()').extract()[0]
        rule = re.compile(r'\d+')
        movie_pid = rule.findall(str(pid))[0]
        url = "https://www.javbus.info/ajax/uncledatoolsbyajax.php?gid=" + str(movie_pid) + "&lang=zh&img=https://pics.javcdn.pw/cover/6dx6_b.jpg&uc=0&floor=153"
        return url

    # def movie_torrent(self,response):
    #     movie_torrent = response.body.decode('utf-8')
    #     torrent = re.compile(r'href="(.*?)"')
    #     movie_torren = torrent.findall(movie_torrent)[0]
    #     #mot = ","
    #     if len(movie_torren) > 0:
    #         mt = movie_torren
    #     else:
    #         mt = "Null"
    #     return mt