# -*- coding: utf-8 -*-
import scrapy
import re


class HpdmissingSpider(scrapy.Spider):
    name = 'hpdmissing'
    allowed_domains = ['www.honolulupd.org']
    #start_urls = ['http://www.honolulupd.org/information/index.php?page=news_archive']
    url_ref = 'http://www.honolulupd.org/information/index.php?page=news_archive'
    limit_pages = 5

    def start_requests(self):
        yield scrapy.Request(url='http://www.honolulupd.org/information/index.php?page=news_archive', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        })


    def parse(self, response):
        source_head = response.xpath('//html/head/title/text()').get()
        source_name = source_head + " " + response.xpath('//p[@class="titletx"]/text()').get().strip()
        news_items = response.xpath('//div[@class="bodytx"]/a[contains(text(), "Missing")]')
        for item in news_items:
            #link_name = item.xpath('.//text()').get()
            abs_link = f"http://www.honolulupd.org{item.xpath('.//@href').get().strip('.')}"

            meta_dict = {
                'source_name': source_name
            }

            yield response.follow(url=abs_link, callback=self.parse_item, meta=meta_dict, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
            })

        next_page = response.xpath('//td[@class="bodytx"]/a/@href').get()

        if next_page:
            try:
                match = re.match(r".*pageNum_data=(\d+)", next_page)
                page_number = int(match.group(1))
            except:
                page_number = self.limit_pages + 10000

            if page_number <= self.limit_pages:
                next_url = f"http://www.honolulupd.org{next_page}"
                yield scrapy.Request(url=next_url, callback=self.parse, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
                })


    def parse_item(self, response):
        source_name = response.request.meta['source_name']
        #link_name = response.request.meta['link_name']
        #abs_link = response.request.meta['abs_link']
        fname = response.xpath('//p[@class="subtitletx" and contains(text(), "Missing")]/text()').get()

        try:
            f1 = re.compile(r"^(Missing.*):\s*(.*)")
            notes_1 = f1.match(fname).group(1)
            fullname = f1.match(fname).group(2)
        except:
            notes_1 = ""
            fullname = fname

        im_1 = response.xpath('//img[@id="new_image"]/@src').get().strip('.')
        image = f"http://www.honolulupd.org{im_1}"
        desc_list = response.xpath('//p[@class="bodytx"]')
        notes_2 = desc_list[1].xpath('.//text()').get()

        yield {
            'source_url': self.url_ref,
            'source_name': source_name,
            'image': image,
            'fullname': fullname,
            'status': notes_1,
            'missing_since':  notes_2
        }