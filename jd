# -*- coding: utf-8 -*-
import scrapy
from ..items import JdItem
from urllib.parse import quote


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    # 初始Url
    base_url = 'https://search.jd.com/Search?keyword='

    def start_requests(self):
        # 得到settings里的KEYWORD
        keyword = self.settings.get("KEYWORD")
        url = self.base_url + quote(keyword)
        for page in range(3):
            params = {
                "page":page+1
            }
            yield scrapy.Request(url=url, callback=self.parse, meta=params,dont_filter=True)
    # def start_requests(self):
    #     for i in range(5):
    #         if (i+1)%2 !=0:
    #             url = self.base_url + str(i+1)
    #             yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = JdItem()
        for i in response.xpath('//*[@id="J_goodsList"]/ul/li'):
            item["title"] = i.xpath(
                "string(./div/div[4]/a/em)").extract_first()
            item["price"] = i.xpath(
                "string(./div/div[3]/strong)").extract_first()
            item["shop"] = i.xpath(
                "string(./div/div[7]/span/a)").extract_first()
            yield item
