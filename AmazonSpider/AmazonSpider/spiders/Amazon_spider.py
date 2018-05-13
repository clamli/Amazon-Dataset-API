import scrapy


class AmazonSpider(scrapy.Spider):
    name = "Amazon"

    def start_requests(self):
        urls = [
            "http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for dataset, url in zip(response.css("table td a::text").extract(), response.css("table td a::attr(href)").extract()):
            yield {
                'dataset': dataset,
                'url': url,
            }



        
        