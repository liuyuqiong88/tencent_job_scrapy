# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from tencent_job.items import TencentJobItem


class TencentJobSpiderSpider(scrapy.Spider):
    name = "tencent_job_spider"
    allowed_domains = ["tencent.com"]
    start_urls = (
        'https://hr.tencent.com/position.php',
    )

    def parse(self, response):

        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        print(11111)
        print(node_list)

        for node in node_list:
            item = TencentJobItem()

            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['detail_url'] = node.xpath('./td[1]/a/@href').extract_first()
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['num'] = node.xpath('./td[3]/text()').extract_first()
            item['address'] = node.xpath('./td[4]/text()').extract_first()
            item['create_date'] = node.xpath('./td[5]/text()').extract_first()

            yield item

        next_url = "https://hr.tencent.com/" +response.xpath('//*[@id="next"]/@href').extract_first()
        print(next_url)
        yield scrapy.Request(next_url)


