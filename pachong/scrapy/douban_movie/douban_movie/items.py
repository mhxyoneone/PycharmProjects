# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_id = scrapy.Field()
    movie_name = scrapy.Field()
    rating_num = scrapy.Field()
    movie_pic = scrapy.Field()
    movie_director = scrapy.Field()
    movie_actors = scrapy.Field()
    movie_type = scrapy.Field()
    movie_introduction = scrapy.Field()