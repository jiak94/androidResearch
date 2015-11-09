# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class ApkcrawlerHotPipeline(object):
	def process_item(self, item, spider):
		if spider.name not in ['anzhihot']:
			return item

		self.file = codecs.open('hot.json', 'a', encoding='utf-8')
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line.decode("unicode_escape"))
		return item

class ApkcrawlerGamePipeline(object):
	def process_item(self, item, spider):
		if spider.name not in ['anzhigame']:
			return item

		self.file = codecs.open("game.json", "a", encoding='utf-8')
		line = json.dumps(dict(item)) + '\n'
		self.file.write(line.decode("unicode_escape"))
		return item
