
import scrapy
from ..items import TencentItem


class TenSpider(scrapy.Spider):
    name = 'ten'
    allowed_domains = ['hr.tencent.com']
    # start_urls = [
    #     'https://hr.tencent.com/position.php'
    # ]
    # 重写start_requests(self)
    def start_requests(self):
        for i in range(1):
            url = "https://hr.tencent.com/position.php?&start="+str(i*10)+"#a"
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # 实例化
        item = TencentItem()
        # 遍历数据所有的tr标签 list去首尾[1:-1]
        for i in response.xpath("//tr")[1:-2]:
            item["name"] = i.xpath("./td[1]/a/text()").extract_first()
            item["p_type"] = i.xpath("./td[2]/text()").extract_first()
            item["person"] = i.xpath("./td[3]/text()").extract_first()
            item["address"] = i.xpath("./td[4]/text()").extract_first()
            item["time"] = i.xpath("./td[5]/text()").extract_first()
            # 返回
            yield item
        # 得到下一页跳转连接
        # next = response.xpath('//*[@id="next"]/@href').extract_first()
        # url = response.urljoin(next)
        # yield scrapy.Request(url=url,callback=self.parse)
