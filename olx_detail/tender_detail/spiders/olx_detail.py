# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 05:27:05 2019

@author: DIBYA
"""
import re
import scrapy
from tender_detail.items import olxdetail
class olx_detail(scrapy.Spider):
    name="olx_details"
    start_urls=['https://www.olx.in/']
    def parse(self,response):
        keywords=["j7 (pro)","Dell XPS 13","Dell XPS 15"]
        for key in keywords:
            word=re.sub(r"\s+",'-',key)
            sub_url="items/q-"+word
            next_url=response.urljoin(sub_url)
            print("**************"+ next_url+"*****")
            yield scrapy.Request(next_url,callback=self.firstpage)
    
    def firstpage(self,response):
         item=olxdetail()
         
         items_list=response.xpath('//li[@data-aut-id="itemBox"]/a/@href').extract()
         for items in items_list:
             new_url=response.urljoin(items)
             item['Product_url']=new_url
             yield scrapy.Request(new_url,callback=self.items_details, meta={'items' : item.copy()})
    def items_details(self,response):
          item=response.meta['items']
          s=response.xpath('//span[@data-aut-id="itemPrice"]/text()').extract()
          print(s)
          item['Price']=s
          item['seller_name']=response.xpath('//div[@class="_3oOe9"]/text()').extract()
          ur=response.xpath('//div[@class="_224W6"]/a/@href').extract()
          sellur=response.urljoin(ur[0])
          item['seller_url']=sellur
          
          return item
          
         
            
            