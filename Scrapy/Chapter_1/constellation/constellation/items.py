# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ConstellationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()

    OverallFortuneTitle = scrapy.Field()
    OverallFortuneContent = scrapy.Field()

    LoveFortuneTitle = scrapy.Field()
    LoveFortuneContent = scrapy.Field()

    CareerFortuneTitle = scrapy.Field()
    CareerFortuneContent = scrapy.Field()

    WealthFortuneTitle = scrapy.Field()
    WealthFortuneContent = scrapy.Field()


    # resolveConstellation = super.Field()

