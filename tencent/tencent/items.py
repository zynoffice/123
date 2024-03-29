# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    #  职位名称	职位类别	人数	地点	发布时间
    name = scrapy.Field()
    p_type = scrapy.Field()
    person = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()
