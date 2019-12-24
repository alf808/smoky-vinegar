# -*- coding: utf-8 -*-
import scrapy
import re


class MissingunsolvedSpider(scrapy.Spider):
    name = 'missingunsolved'
    allowed_domains = ['www.missingandunsolved.com']
    start_urls = ['http://www.missingandunsolved.com/hawaii/']
    #used User-Agent specified in settings.py

    def parse(self, response):
        source_name = response.xpath('//html/head/title/text()').get()
        #source_name = source_head + " " + response.xpath('//h1/a/text()').get().strip()
        
        listing = response.xpath('//li[@class="listing-item"]')
        #fb_listing = response.xpath('//div[@data-page-id="HawaiiLostNMissing"]')
        #fb_listing = response.xpath('//div[@class="cff-text-wrapper"]')
        fb_listing = response.xpath('//p[@class="cff-post-text"]')

        for item in listing: 
            image = item.xpath('a[@class="image"]/img/@src').get()
            fullname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
            age = item.xpath('span[@class="excerpt"]/text()').re(r'Age.*:\s*(\d*),')[0]
            missing_since = item.xpath('span[@class="excerpt"]/text()').re(r'(\d{1,2}/\d{1,2}/\d{4})')[0]
            notes = item.xpath('span[@class="excerpt"]/text()').get().strip().title()

            yield {
                'source_url': self.start_urls[0],
                'source_name': source_name,
                'image': image,
                'fullname': fullname,
                'gender': '',
                'race': '',
                'dob': '',
                'age': age,
                'height': '',
                'weight': '',
                'hair': '',
                'eye': '',
                'missing_since': missing_since,
                'last_know_loc': notes
            }
        

        for item in fb_listing: 
            n1 = item.xpath('.//span[@class="cff-text"]/node()').getall() 
            n1_list = [x.strip() for x in n1] 
            x = n1_list[0] 
            re1 = re.search(r"^#.*Missing", x) 
            re2 = re.search(r"^<a.*#.*Missing", x) 
            if re1: 
                try: 
                    c1 = re.compile(r"^#.*Missing\s*(.*),\s*(\d*),\s*(.*)") 
                    fullname = c1.match(x).group(1) 
                    age = c1.match(x).group(2) 
                    notes = c1.match(x).group(3) 
                except: 
                    #print('within re1') 
                    fullname, age, notes, notes_2 = ("", 0, "", " ".join(n1_list)) 
                else: 
                    #print(fullname, age, notes, sep=';') 
                    notes_2 = " ".join(n1_list[1:]) 
            elif re2: 
                x2 = n1_list[1] 
                try: 
                    c1 = re.compile(r"(.*),\s*(\d*),\s*(.*)") 
                    fullname = c1.match(x2).group(1) 
                    age = c1.match(x2).group(2) 
                    notes = c1.match(x2).group(3) 
                except: 
                    try: 
                        c1 = re.compile(r"(.*?),(.*)") 
                        fullname = c1.match(x2).group(1) 
                        age = 0 
                        notes = c1.match(x2).group(2) 
                    except: 
                        #print(x2) 
                        fullname, age, notes, notes_2 = ("", 0, "", " ".join(n1_list)) 
                    else: 
                        #print(fullname, notes, sep=';') 
                        notes_2 = " ".join(n1_list[2:]) 
                else: 
                    #print(fullname, age, notes, sep=';') 
                    notes_2 = " ".join(n1_list[2:]) 
            else: 
                #print(x) 
                fullname, age, notes, notes_2 = ("", 0, "", " ".join(n1_list)) 

            yield {
                'source_url': self.start_urls[0],
                'source_name': source_name,
                'image': '',
                'fullname': fullname,
                'gender': '',
                'race': '',
                'dob': '',
                'age': age,
                'height': '',
                'weight': '',
                'hair': '',
                'eye': '',
                'missing_since': notes,
                'last_know_loc': notes_2
            }
