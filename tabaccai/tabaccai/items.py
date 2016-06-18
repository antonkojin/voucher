# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TabaccaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    indirizzo = scrapy.Field()
    cap = scrapy.Field()
    comune = scrapy.Field()
    provincia = scrapy.Field()