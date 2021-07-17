import scrapy
from theguardian.items import TheguardianItem

class TheguardianNewsSpider(scrapy.Spider):
    name = 'theguardian_news'
    allowed_domains = ['theguardian.com']

    theguardian_urls = ['world/coronavirus-outbreak', 'world', 'uk-news', 'uk/environment', 'uk/environment', 'science',
                        'global-development', 'football', 'uk/technology', 'uk/business', 'tone/obituaries']

    start_urls = ['https://www.theguardian.com/' + sub + '/all' for sub in theguardian_urls]

    def parse(self, response):
        article_headline = response.xpath("//div[@class='fc-item__container']/a/text()").extract()
        article_timestamp = response.xpath("//div[@class='fc-item__standfirst-wrapper fc-item__standfirst-wrapper--timestamp']/div/time/@datetime").extract()
        article_url = response.xpath("//div[@class='fc-item__container']/a/@href").extract()

        row_data = zip(article_headline, article_timestamp, article_url)

        # Making extracted data row wise
        for data in row_data:
            item = TheguardianItem()
            item['page'] = response.url
            item['article_headline'] = data[0]
            item['article_timestamp'] = data[1]
            item['article_url'] = data[2]
            item['article_tag'] = data[2].split("/")[3]

            # yield or give the scraped info to scrapy
            yield item

            next_page = response.xpath("//div[3]/div/div[3]/div/div/a[4]/@href").extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)

