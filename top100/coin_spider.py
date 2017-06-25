import scrapy

class CoinSpider(scrapy.Spider):
    name = "coins"
    allowed_domains = ["https://coinmarketcap.com/"]
    start_urls = [
    "https://coinmarketcap.com/",
    ]

    def parse(self, response):
        null = None
        for line in response.css('tr'):
            yield{
                'number' : line.xpath('td[1]/text()').extract_first(),
                'name' : line.xpath('td[2]/a/text()').extract_first(),
                'marketCap' : line.xpath('td[3]/text()').extract_first(),
                'price' : line.xpath('td[4]/a/text()').extract_first(),
                'circulatingSupply' : line.xpath('td[5]/a/text()').extract_first(),
                'volume' : line.xpath('td[6]/a/text()').extract_first(),
                'percentChange' : line.xpath('td[7]/text()').extract_first()
            } 