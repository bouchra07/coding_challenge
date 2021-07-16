import scrapy


class TheguardianNewsSpider(scrapy.Spider):
    name = 'theguardian_news'
    allowed_domains = ['theguardian.com']
    start_urls = ['http://www.theguardian.com/world/coronavirus-outbreak/all/']

    def parse(self, response):
        pass
