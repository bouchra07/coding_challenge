# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class TheguardianItem(scrapy.Item):
    page = Field()
    article_headline = Field()
    article_timestamp = Field()
    article_url = Field()
    article_tag = Field()






