import scrapy
import json
import codecs
import requests
from bs4 import BeautifulSoup

from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import log

from apkcrawler.items import ApkcrawlerItem

class anzhiCrawlerHot(scrapy.Spider):
	name = "anzhihot"
	allowed_domains = ["anzhi.com"]
	start_urls = [
		 "http://www.anzhi.com/list_1_1_hot.html",
		 "http://www.anzhi.com/list_1_2_hot.html",
		 "http://www.anzhi.com/list_1_3_hot.html",
		 "http://www.anzhi.com/list_1_4_hot.html",
		 "http://www.anzhi.com/list_1_5_hot.html",
		 "http://www.anzhi.com/list_1_6_hot.html",
		 "http://www.anzhi.com/list_1_7_hot.html",
		 "http://www.anzhi.com/list_1_8_hot.html",
		 "http://www.anzhi.com/list_1_9_hot.html",
		 "http://www.anzhi.com/list_1_10_hot.html",
		 "http://www.anzhi.com/list_1_11_hot.html",
		 "http://www.anzhi.com/list_1_12_hot.html",
		 "http://www.anzhi.com/list_1_13_hot.html",
		 "http://www.anzhi.com/list_1_14_hot.html",
		 "http://www.anzhi.com/list_1_15_hot.html",
		 "http://www.anzhi.com/list_1_16_hot.html",
		 "http://www.anzhi.com/list_1_17_hot.html",
		 "http://www.anzhi.com/list_1_18_hot.html",
		 "http://www.anzhi.com/list_1_19_hot.html",
		 "http://www.anzhi.com/list_1_20_hot.html",
		 "http://www.anzhi.com/list_1_21_hot.html",
		 "http://www.anzhi.com/list_1_22_hot.html",
		 "http://www.anzhi.com/list_1_23_hot.html",
		 "http://www.anzhi.com/list_1_24_hot.html",
		 "http://www.anzhi.com/list_1_25_hot.html",
		 "http://www.anzhi.com/list_1_26_hot.html",
		 "http://www.anzhi.com/list_1_27_hot.html",
		 "http://www.anzhi.com/list_1_28_hot.html",
		 "http://www.anzhi.com/list_1_29_hot.html",
		 "http://www.anzhi.com/list_1_30_hot.html",
		 "http://www.anzhi.com/list_2_1_hot.html",
		 "http://www.anzhi.com/list_2_2_hot.html",
		 "http://www.anzhi.com/list_2_3_hot.html",
		 "http://www.anzhi.com/list_2_4_hot.html",
		 "http://www.anzhi.com/list_2_5_hot.html",
		 "http://www.anzhi.com/list_2_6_hot.html",
		 "http://www.anzhi.com/list_2_7_hot.html",
		 "http://www.anzhi.com/list_2_8_hot.html",
		 "http://www.anzhi.com/list_2_9_hot.html",
		 "http://www.anzhi.com/list_2_10_hot.html",
		 "http://www.anzhi.com/list_2_11_hot.html",
		 "http://www.anzhi.com/list_2_12_hot.html",
		 "http://www.anzhi.com/list_2_13_hot.html",
		 "http://www.anzhi.com/list_2_14_hot.html",
		 "http://www.anzhi.com/list_2_15_hot.html",
		 "http://www.anzhi.com/list_2_16_hot.html",
		 "http://www.anzhi.com/list_2_17_hot.html",
		 "http://www.anzhi.com/list_2_18_hot.html",
		 "http://www.anzhi.com/list_2_19_hot.html",
		 "http://www.anzhi.com/list_2_20_hot.html",
		 "http://www.anzhi.com/list_2_21_hot.html",
		 "http://www.anzhi.com/list_2_22_hot.html",
		 "http://www.anzhi.com/list_2_23_hot.html",
		 "http://www.anzhi.com/list_2_24_hot.html",
		 "http://www.anzhi.com/list_2_25_hot.html",
		 "http://www.anzhi.com/list_2_26_hot.html",
		 "http://www.anzhi.com/list_2_27_hot.html",
		 "http://www.anzhi.com/list_2_28_hot.html",
		 "http://www.anzhi.com/list_2_29_hot.html",
	     "http://www.anzhi.com/list_2_30_hot.html",
	]

	def parse(self, response):
		items = []
		for sel in response.xpath("//div[@class='content_left']/div[@class='app_list border_three']/ul/li"):
			item = ApkcrawlerItem()
			#apk
			apk_name = sel.xpath("div[@class='app_info']/span[@class='app_name']/a/text()").extract()
			item['file_name'] = [n.encode('utf-8') for n in apk_name]
			#desc link
			desc = sel.xpath("div[@class='app_info']/span[@class='app_name']/a/@href").extract()
			desc.insert(0, "http://www.anzhi.com")
			item['desc_link'] = desc[0] + desc[1]
			#download link
			apk_id = sel.xpath("div[@class='app_down']/a/@onclick").extract()[0]
			apk_id = apk_id[apk_id.find("(")+1:apk_id.rfind(")")]
			down_link = "http://www.anzhi.com/dl_app.php?s=" + apk_id + "&n=5"
			item['file_urls'] = [down_link]
			#category
			r = requests.get(item['desc_link'])
			soup = BeautifulSoup(r.text)
			category = soup.find("ul", id="detail_line_ul").li.extract()
			item['category'] = [n.encode('utf-8') for n in category]
			items.append(item)

		return items
