# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
import lxml
from javbud_spider.items import JavbudSpiderItem
import re
import requests
class Jav1Spider(scrapy.Spider):
    name = 'jav_1'
    allowed_domains = ['javbus.info']
    #start_urls = ['https://www.javbus.info/ajax/uncledatoolsbyajax.php?gid=36423543929&lang=zh&img=https://pics.javcdn.pw/cover/6dx6_b.jpg&uc=0&floor=153']
    start_urls = ['#######']
    # def make_requests_from_url(self, url):
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.text,'lxml')
    #     return soup.contents
    headers = {
        'authority': '#######',
        'method': 'GET',
        'path': '/ajax/uncledatoolsbyajax.php?gid=36417994212&lang=zh&img=https://pics.javcdn.pw/cover/6f58_b.jpg&uc=0&floor=280',
        'scheme': 'https',
        'accept': '*/*',
        # 'accept-encoding':'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__cfduid=dbc14b3bc854c776636d1035548a5f54e1516261025; HstCfa3288802=1516261062336; HstCmu3288802=1516261062336; __dtsu=2DE7B66BC84E605AC20C3E85029CA511; PHPSESSID=4jvt428b36d9jjd4npc5vism55; HstCla3288802=1518094188397; HstPn3288802=1; HstPt3288802=19; HstCnv3288802=4; HstCns3288802=6',
        'referer': '#######/#####',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    def parse(self, response):
        #items = JavbudSpiderItem()
        urls = response.xpath('//a[@class="movie-box"]/@href').extract()
        for url in urls:
            print('第一层爬取')
            print(url)
            yield scrapy.Request(url=url,callback=self.parse_two)

    def parse_two(self,response):
        items = JavbudSpiderItem()
        pid = response.xpath('/html/body/script[3]/text()').extract()[0]
        rule = re.compile(r'\d+')
        movie_pid = rule.findall(str(pid))[0]
        url = "https://www.javbus.info/ajax/uncledatoolsbyajax.php?gid=" + movie_pid + "&lang=zh&img=https://pics.javcdn.pw/cover/6dx6_b.jpg&uc=0&floor=153"
        print(url)
        print('第二层爬取')
        items['movie_torrent'] = self.parse_third(url)
        yield items

    def parse_third(self,url):
        print('第三层爬取')
        response = requests.get(url, headers=self.headers)
        response1 = response.text
        #movie_torrent = response.body.decode('utf-8')
        torrent = re.compile(r'href="(.*?)"')
        magent =torrent.findall(response1)
        return magent