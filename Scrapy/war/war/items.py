# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WarItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    date = scrapy.Field()
    lieu = scrapy.Field()
    issue = scrapy.Field()
    description = scrapy.Field()
    belligerents = scrapy.Field()
    pass
