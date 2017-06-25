import scrapy

class CoinSpider(scrapy.Spider):
    name = "coins"
    allowed_domains = ["https://coinmarketcap.com/all/views/all/"]
    start_urls = [
    "https://coinmarketcap.com/all/views/all/",
    ]

    def parse(self, response):
        for line in response.css('tr'):
            yield{
                'number' : line.xpath('td[1]/text()').extract_first(),
                'name' : line.xpath('td[2]/a/text()').extract_first(),
                'symbol' : line.xpath('td[3]/text()').extract_first(),
                'marketCap' : line.xpath('td[4]/text()').extract_first(),
                'price' : line.xpath('td[5]/a/text()').extract_first(),
                'circulatingSupply' : line.xpath('td[6]/a/text()').extract_first(),
                'volume24' : line.xpath('td[7]/a/text()').extract_first(),
                '%1h' : line.xpath('td[8]/text()').extract_first(),
                '%24h' : line.xpath('td[9]/text()').extract_first(),
                '%7d' : line.xpath('td[10]/text()').extract_first(),
            } 