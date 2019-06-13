# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client["tencent"]
t = db["item"]


class TencentPipeline(object):
    def process_item(self, item, spider):
        return item

# 写入txt


class TxtPipeline(object):
    def process_item(self, item, spider):
        with open("item.txt", "a", encoding="utf-8") as f:
            # 把item强转成str
            f.write(str(item)+"\n")
        return item
# 存入数据库


class MongoPipeline(object):
    # 爬虫启动时调用
    def open_spider(self, spider):
        print("爬虫启动了调用")
    # 爬虫关闭时调用

    def close_spider(self, spider):
        print("爬虫关闭了调用")
        client.close()
    def process_item(self, item, spider):
        # 插入数据
        t.insert_one(dict(item))
        return item
