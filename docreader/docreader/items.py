# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DocreaderItem(scrapy.Item):
    # define the fields for your item here like:
    sub_section = scrapy.Field()
    subsub_section = scrapy.Field()
    readtime = scrapy.Field()
    url = scrapy.Field()
