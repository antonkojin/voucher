# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = "indirizzi"
    start_urls = [
        'http://serviziweb.tabaccai.it/voucherinps/VistaAdesioni.aspx',
    ]

    def parse(self, response):
        self.logger.info("page: " + response.body)
