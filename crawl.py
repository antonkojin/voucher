#!/usr/bin/env python2

from scrapy.crawler import CrawlerProcess
from tabaccai.tabaccai.spiders.addresses import AddressesSpider

def crawl(comune):
    process = CrawlerProcess()
    process.crawl(AddressesSpider, comune=comune)
    process.start()


crawl("milano")
