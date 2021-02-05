import scrapy
import json
from pymongo import MongoClient


class Yad2Spider(scrapy.Spider):
    api_url = 'https://www.yad2.co.il/api/item/{item_id}'
    name = 'yad2'
    item_filter = 'div.feeditem div.feed_item-v4::attr(itemid)'
    query = 'https://www.yad2.co.il/vehicles/private-cars?manufacturer=13&model=97'
    start_urls = [query]
    next_page_filter = 'a.next::attr(href)'
    filename = '/data.nobackup/workspace/py-workspace/yad2/yad2-data/'
    cars_collection = None

    def parse(self, response):
        """
            The parse methods parse the yad2 result page,
            For each car send another request with the car id the getthe car information.
            For each car api result call the parse_item method
            And check in the end if there is a next page if there is its sends another request with the next page url
        """
        print(response.body.decode())
        if 'api' in response.url:
            self.parse_item(response)
        else:
            for item_id in response.css(self.item_filter).getall():
                if item_id is not None:
                    yield scrapy.Request(self.api_url.format(item_id=item_id), callback=self.parse)
            next_page = response.css(self.next_page_filter).get()
            if next_page != response.url and next_page is not None:
                yield scrapy.Request(next_page, callback=self.parse)

    def _get_cars_collection(self):
        if self.cars_collection is None:
            client = MongoClient('localhost', 27017)
            yad2_db = client.yad2
            self.cars_collection = yad2_db.cars
        return self.cars_collection

    def parse_item(self, response):
        cars_collection = self._get_cars_collection()
        item_id = response.url.split('/')[-1]
        if not list(cars_collection.find({'item_id':item_id})):
            result = json.loads(response.body.decode('utf-8'))
            result['item_id'] = item_id
            cars_collection.insert_one(result)
