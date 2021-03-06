# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ApkcrawlerItem(scrapy.Item):
    file_name = scrapy.Field()
    file_urls = scrapy.Field()
    desc_link = scrapy.Field()
    category = scrapy.Field()
    files = scrapy.Field()
