#!/usr/bin/python3.7
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "yad2"
    start_urls = [
        'https://www.yad2.co.il/vehicles/private-cars',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
