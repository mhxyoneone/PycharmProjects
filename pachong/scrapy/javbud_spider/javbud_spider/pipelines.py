# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JavbudSpiderPipeline(object):
    def process_item(self, item, spider):
        mysql = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="mysql",charset="utf8")
        cur = mysql.cursor()
        db = "insert into java_bus(movie_name,movie_id,movie_actor,movie_span,movie_pic,movie_torrent)VALUES ('%s','%s','%s','%s','%s','%s')"%(item['movie_name'],item['movie_id'],item['movie_actor'],item['movie_span'],item['movie_pic'],item['movie_torrent'])

        cur.execute(db)
        mysql.commit()

        mysql.close()
        return item

