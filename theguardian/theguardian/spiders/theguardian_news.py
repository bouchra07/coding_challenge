import scrapy


class TheguardianNewsSpider(scrapy.Spider):
    name = 'theguardian_news'
    allowed_domains = ['theguardian.com']
    start_urls = ['http://www.theguardian.com/world/coronavirus-outbreak/all/']

    def parse(self, response):
        article_headline = response.xpath("//div[@class='fc-item__container']/a/text()").extract()
        article_timestamp = response.xpath("//div[@class='fc-item__standfirst-wrapper fc-item__standfirst-wrapper--timestamp']/div/time/@datetime").extract()
        article_url = response.xpath("//div[@class='fc-item__container']/a/@href").extract()

        row_data = zip(article_headline, article_timestamp, article_url)

        # Making extracted data row wise
        for item in row_data:
            # create a dictionary to store the scraped info
            scraped_info = {
                # key:value
                'page': response.url,
                'article_headline': item[0],
                # item[0] means product in the list and so on, index tells what value to assign
                'article_timestamp': item[1],
                'article_url': item[2],
            }
            # yield or give the scraped info to scrapy
            yield scraped_info

            next_page = response.xpath("//div[3]/div/div[3]/div/div/a[4]/@href").extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse)

