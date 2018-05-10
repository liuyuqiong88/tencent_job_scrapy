# -*- coding: utf-8 -*-
import scrapy


class RenfromSpider(scrapy.Spider):
    name = 'renfrom'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        login_url = response.xpath('//*[@id="loginForm"]/@action').extract_first()
        print(111111111111111,login_url)

        post_data = {
            "email":"17173805860",
            "password":"1qaz@WSX3edc",
        }
        yield scrapy.FormRequest(
            url=login_url,
            formdata=post_data,
            callback=self.parse_index
        )

    def parse_index(self,response):

        with open('renren_from.html', 'wb')as f:
            f.write(response.body)
