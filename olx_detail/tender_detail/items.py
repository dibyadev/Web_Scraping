
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

	
class olxdetail(scrapy.Item):
    Product_url=scrapy.Field()
    Price=scrapy.Field()
    seller_name=scrapy.Field()
    seller_url=scrapy.Field()

	

