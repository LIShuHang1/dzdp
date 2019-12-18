# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://www.dianping.com/beijing/ch95/g25147']

    def parse(self, response):
        pass
