
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TenderDetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class details1(scrapy.Item):
    closing_date=scrapy.Field()
    title=scrapy.Field()
    address=scrapy.Field()
    abstract=scrapy.Field()
    status=scrapy.Field()

    Organization=scrapy.Field()
    categories=scrapy.Field()
    linkTo=scrapy.Field()
    competitionNumber=scrapy.Field()
    bidders=scrapy.Field()
	


	

