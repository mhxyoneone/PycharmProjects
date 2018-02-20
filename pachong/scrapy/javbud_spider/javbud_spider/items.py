# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavbudSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name = scrapy.Field()
    movie_id = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_span = scrapy.Field()
    movie_pic = scrapy.Field()
    movie_torrent = scrapy.Field()
    #movie_pid_url = scrapy.Field()
