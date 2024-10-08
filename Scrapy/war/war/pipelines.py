# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WarPipeline:# fonction de cyble de vie
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
        )

    def open_spider(self, spider): # fonction de cycle de vie
        # fonction qui s'appelle au debut de l'execution du spider
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider): # fonction de cycle de vie
        # fonction qui s'appelle a la fin de l'execution du spider
        self.client.close()

    def process_item(self, item, spider):
        collection_name = spider.name
        self.db[collection_name].insert_one(ItemAdapter(item).asdict())
        return item
