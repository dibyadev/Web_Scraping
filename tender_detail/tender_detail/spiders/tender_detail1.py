# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:21:09 2019

@author: DIBYA
"""
import scrapy
from tender_detail.items import details1
class tender_detail1(scrapy.Spider):
    name="tender_module"
    start_urls=['https://www.princeedwardisland.ca/en/tenders/']
    count=0
    def parse(self,response):
        item=details1()
        u="https://www.princeedwardisland.ca/en/tenders/"
        yield scrapy.Request(u,callback=self.firstPage, meta={'items' : item.copy()})
        a=response.xpath('//li[@class="pager-next"]/a/@href').extract()
        for an in a:
            ur=response.urljoin(an)
        yield scrapy.Request(ur,callback=self.nextPage, meta={'items' : item.copy()})
    
         
    def nextPage(self,response):
        item=response.meta['items']
        self.count+=1
        i=0
        clos=response.xpath('//span[@class="date-display-single"]/text()').extract()
        cat=response.xpath('//div[@class="views-field views-field-field-t-tender-category-tax"]/span[@class="field-content"]/text()').extract()
        links=response.xpath('//div[@class="item-list"]/ul/li/div/span/a/@href').extract()
        for link in links:
                item['closingDate']=clos[i]
                item['categories']=cat[i]
                next_url=response.urljoin(link)
                i+=1
                yield scrapy.Request(next_url,callback=self.parseDetail, meta={'items' : item.copy()})
        if(self.count!=5):
            try:
                
                a=response.xpath('//li[@class="pager-next"]/a/@href').getall()
            except:
                a = "None"
#        
            if(a is not None):
                for n in a:
                    nextpage_url=response.urljoin(n)
                    yield scrapy.Request(nextpage_url,callback=self.firstPage , meta={'items' : item.copy()})
            else:
                print("Next")
            
        else:
             print("next")
    
    def firstPage(self,response): 
        item=response.meta['items']
        i=0
        clos=response.xpath('//span[@class="date-display-single"]/text()').extract()
        cat=response.xpath('//div[@class="views-field views-field-field-t-tender-category-tax"]/span[@class="field-content"]/text()').extract()
        links=response.xpath('//div[@class="item-list"]/ul/li/div/span/a/@href').extract()
        for link in links:
                item['closingDate']=clos[i]
                item['categories']=cat[i]
                next_url=response.urljoin(link)
                i+=1
                yield scrapy.Request(next_url,callback=self.parseDetail, meta={'items' : item.copy()})
#            
        try:
            a=response.xpath('//li[@class="pager-next"]/a/@href').getall()
        except:
            a = "None"
        
        if(a is not None):
            for n in a:
                nextpage_url=response.urljoin(n)
            yield scrapy.Request(nextpage_url,callback=self.nextPage,  meta={'items' : item.copy()})
        else:
            print("Next")   
            
    
    def parseDetail(self,response):
        item=response.meta['items']
        item['1title']=response.xpath('//div[@class="panel-pane pane-page-title"]/div/h1/text()').extract()
        item['organization_name']=response.xpath('//div[@class="field field-name-field-t-organization field-type-entityreference field-label-above"]/div[@class="field-items"]/div/text()').extract()
        hiper_link=response.xpath('//div[@class="field field-name-field-file-single field-type-file field-label-above"]/div[2]/div/span/a/@href').extract()
        for h in hiper_link:
            item['linkTo']=response.urljoin(h)
        item['competitionNumber']=response.xpath('//div[@class="field field-name-field-t-solicitation-number field-type-text field-label-above"]/div[@class="field-items"]/div/text()').extract()
        item['bidders']={
                'contactName': response.xpath('//div[@class="field field-name-field-t-contact-2 field-type-text field-label-hidden"]/div[@class="field-items"]/div/text()').extract()
                , 'contactEmail': response.xpath('//div[@class="field field-name-field-t-email-address field-type-email field-label-hidden"]/div[@class="field-items"]/div/a/text()').extract()
                , 'contact tel': response.xpath('//div[@class="field field-name-field-t-phone-number field-type-phone field-label-inline clearfix"]/div[@class="field-items"]/div/text()').extract()
                }

        return item
            
        