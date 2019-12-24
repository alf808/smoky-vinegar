# -*- coding: utf-8 -*-
import scrapy

class HnlcrimestopSpider(scrapy.Spider):
    name = 'hnlcrimestop'
    allowed_domains = ['honolulucrimestoppers.org']
    start_urls = ['http://honolulucrimestoppers.org/sitemenu.aspx?P=missing&ID=606']
    #used User-Agent specified in settings.py
    
    def parse(self, response):
        source_head = response.xpath('//html/head/title/text()').get()
        source_name = source_head + " " + response.xpath('//h3/text()').get().strip()
        #persons = response.xpath('//div[@id="divMainBody"]/div/div/div').getall()
        images = response.xpath('//img[@class="img-responsive"]/@src').getall()
        names = response.xpath('//tbody/tr[1]/td[2]/span/text()').getall()
        genders = response.xpath('//tbody/tr[2]/td[2]/text()').getall()
        races = response.xpath('//tbody/tr[2]/td[5]/text()').getall()
        dobs = response.xpath('//tbody/tr[3]/td[2]/text()').getall()
        ages = response.xpath('//tbody/tr[3]/td[5]/text()').getall()
        heights = response.xpath('//tbody/tr[4]/td[2]/text()').getall()
        weights = response.xpath('//tbody/tr[4]/td[5]/text()').getall()
        hairs = response.xpath('//tbody/tr[5]/td[2]/text()').getall()
        eyes = response.xpath('//tbody/tr[5]/td[5]/text()').getall()
        notes_1 = response.xpath('//tbody/tr/td/div[@xstyle="font-size:16px;color:#23539F;font-weight:bold;line-height: 1.2"]/text()').getall()
        notes_2 = response.xpath('//tbody/tr/td/div[@xstyle="color:#aaaaaa;font-size:10px;line-height: 1.2"]/text()').getall()
        
        desc = [item.strip() for item in notes_1]
        missing_date = [item.strip(':').strip() for item in notes_2]
        
        missing_persons = zip(images, names, genders, races, dobs, ages, heights, weights, hairs, eyes, desc, missing_date)

        for detail in missing_persons:

            yield {
                'source_url': self.start_urls[0],
                'source_name': source_name,
                'image': detail[0],
                'fullname': detail[1],
                'gender': detail[2],
                'race': detail[3],
                'dob': detail[4],
                'age': detail[5],
                'height': detail[6],
                'weight': detail[7],
                'hair': detail[8],
                'eye': detail[9],
                'last_know_loc': detail[10],
                'missing_since': detail[11]
            }

