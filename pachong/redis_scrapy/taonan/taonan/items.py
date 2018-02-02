# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaonanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    age = scrapy.Field()
    header_pic = scrapy.Field()
    image_pic = scrapy.Field()
    content = scrapy.Field()
    place_from = scrapy.Field()
    education = scrapy.Field()
    user_url = scrapy.Field()
    sourceurl = scrapy.Field()


