# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from .settings import MONGO_URI


class TianyanchaPipeline_mongodb(object):
    def __init__(self):
        self.client = pymongo.MongoClient(MONGO_URI)
        self.db = self.client['tianyancha']
        self.col = self.db['cha']

    def process_item(self, item, spider):
        self.col.insert_one(dict(item))
        return item
