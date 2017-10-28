# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field


class ZhangTuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = Field()
    ticket = Field()
    scenicSpot = Field()
    location = Field()
    img = Field()
    url = Field()
    city = Field() 

class PizerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass