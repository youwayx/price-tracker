import scrapy
#from amazon.items import AmazonItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class AmazonSpider(scrapy.Spider):
    name = "amazon_cool"
    allowed_domains = ["amazon.com"]
    start_urls= ["http://www.amazon.com/Fire-TV-streaming-media-player/dp/B00CX5P8FC"]
    #start_urls=["http://www.amazon.com/Amazon-W87CUN-Fire-TV-Stick/dp/B00GDQ0RMG"]
    def parse(self, response):
        for price in response.xpath('//*[@id="priceblock_ourprice"]'):
            print(price.xpath('text()').extract())
            item=AmazonItem()
            item['price']=price.xpath('text()').extract()
            yield item

process = CrawlerProcess(get_project_settings())

process.crawl(AmazonSpider)
#process.start()
