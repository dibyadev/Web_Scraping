# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 06:29:46 2019

@author: DIBYA
"""

import scrapy
from tender_detail.items import details1
class cityOfToronto(scrapy.Spider):
    name="CityOfToronto"
    start_urls=['https://wx.toronto.ca/inter/pmmd/calls.nsf/construction?OpenView']
    def parse(self,response):
        item=details1()
        u=response.xpath('//td[@width="20%"]/div/a/@href').extract()[0]
        url=response.urljoin(u)
        yield scrapy.Request(url,callback=self.firstPage, meta={'items' : item.copy()})
    
    def firstPage(self,response):
        item=response.meta['items']
        i=0
        t=response.xpath("//font[@color='#008000']/text()").extract()
        links=response.xpath("//font[@color='#008000']/a/@href").extract()
        for link in links:
            item['title']=t[i]
            next_urls=response.urljoin(link)
            i+=1
            yield scrapy.Request(next_urls,callback=self.detailPage, meta={'items' : item.copy()})
    
    def detailPage(self,response):
        item=response.meta['items']
        item['closing_date']=response.xpath('//td/b/font[text()="Closing date:"]/ancestor::td/following-sibling::td/b/font/text()').extract()[0]
        item['address']=response.xpath('//td[@width="202"]/font/text()').extract()[1]
        item['abstract']=" ".join(response.xpath('//td[@width="778"]/font/p/text()').extract())
        item['status']="***"
        post=response.xpath('//td[@width="526"]/font//a/@href').extract()
        post.remove('http://www.adobe.com/products/acrobat/readstep.html')
        l=[]
        for po in post:
            po=response.urljoin(po)
            l.append(po)
        item['linkTo']=l
        item['Organization']=response.xpath('//td[@width="192"][2]/font/text()').extract()[0]
        item['competitionNumber']=response.xpath('//td/b/font[text()="Call number:"]/ancestor::td/following-sibling::td/b/font/text()').extract()
        item['categories']="".join(response.xpath('//td[@width="526"]/b/font/text()').extract())
        
        return item
        
        