# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JuziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #head部分
    #公司名称
    company_name = scrapy.Field()
    #公司id
    company_id = scrapy.Field()
    #公司口号
    slogan = scrapy.Field()
    #分类
    scope = scrapy.Field()
    # #子分类
    # sub_scope = scrapy.Field()
    #公司主页
    home_page = scrapy.Field()
    #公司标签
    tags = scrapy.Field()
    #body部分
    #公司全称
    company__full_name = scrapy.Field()
    #公司简介
    company__info = scrapy.Field()
    #成立时间
    found_time = scrapy.Field()
    #公司规模
    company__size = scrapy.Field()
    #运营状态
    company__status = scrapy.Field()
    #end部分
    #融资情况
    tz_info = scrapy.Field()
    #团队情况
    team_info = scrapy.Field()
    #产品信息
    pro_info = scrapy.Field()
