# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    title_text = scrapy.Field()
    send_time = scrapy.Field()
    # review = scrapy.Field()
    id = scrapy.Field()
    review_text = scrapy.Field()
