 1/1: fetch("quotes.toscrape.com")
 1/2: fetch("http://quotes.toscrape.com/")
 1/3: response
 1/4: response.css("h1")
 1/5: response.css("h1::text")
 1/6: response.xpath("//h1")
 1/7: response.xpath("//h1/a/text()")
 1/8: response.xpath("//h1/a/text()").extract()
 1/9: response.xpath("//h1/a/text()").extract_first()
1/10: response.xpath('//*[@class="tag"]')
1/11: response.xpath('//span[@class="tag-item"]')
1/12: response.xpath('//span[@class="tag-item"]/a')
1/13: response.xpath('//span[@class="tag-item"]/a/text()')
1/14: response.xpath('//span[@class="tag-item"]/a/text()').extract()
 2/1: response
 2/2: fetch("http://quotes.toscrape.com/")
 2/3: response.xpath('//h1/a/text()').extract()
 2/4: response.xpath('//h1/a/text()')
 2/5: from scrapy.selector import Selector
 2/6: %paste
 2/7: sel = Selector(text=html_doc)
 2/8: sel.xpath('//h3/text()')
 2/9: sel.xpath('//h3/text()').extract()
2/10: sel.xpath('//h3/text()').extract_first().strip()
2/11: sel.xpath('//html/head/title/text()').extract_first()
 3/1: fetch("http://www.honolulucrimestoppers.org/sitemenu.aspx?ID=606&P=missing")
 3/2: response
 3/3: response.xpath('//h3/text()').get().strip()
 3/4: persons = response.xpath('//div[@class="row no-gutter"]').get()
 3/5: persons
 3/6: len(persons)
 3/7: persons = response.xpath('//div[@class="col-xs-12 col-sm-12"').get()
 3/8: persons = response.xpath('//div[@class="col-xs-12 col-sm-12"]').get()
 3/9: len(persons)
3/10: persons = response.xpath('//div[@class="container-custom"]/div[@class="row"]/div[@class="col-xs-12 col-sm-12"]').get()
3/11: len(persons)
3/12: persons = response.xpath('//div[@id="divMainBody"]').get()
3/13: len(persons)
3/14: persons = response.xpath('//div[@id="divMainBody"]')
3/15: len(persons)
3/16: persons
3/17:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = response.xpath('//tbody')
    for row in details:
        full_name = row.xpath('//td[2]/text()').get()
        yield {
            'img': img,
            'name': full_name
        }
3/18:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = response.xpath('//tbody')
    for row in details:
        full_name = row.xpath('//td[2]/text()').get()
        
        yield {
            'img': img,
            'name': full_name
        }
3/19:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = response.xpath('//tbody')
    yield {'img': img}
3/20:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = response.xpath('//tbody')
3/21: img
3/22: details
3/23: len(details)
3/24:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//tbody')
3/25: img
3/26: details
3/27:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//tbody')
    for row in details:
        full_name = row.xpath('//td[2]/text()').get()
        
        yield {
            'img': img,
            'name': full_name
        }
3/28:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//tbody')
    yield {
        'img': img,
        'deets': details
        }
3/29:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//tbody')
    yield {
        'img': img,
        'deets': details
    }
3/30:
for person in persons:
    img = person.xpath('//img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//tbody')
    for row in details:
        full_name = row.xpath('//td[2]/text()').get()
        
        print(img, full_name)
 4/1: fetch("http://www.honolulucrimestoppers.org/sitemenu.aspx?ID=606&P=missing")
 4/2: import scrapy
 4/3: import scrapy
3/31:
for person in persons:
    img = person.xpath('//div[@class="col-sm-5"]/div/img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//tbody')
    for row in details:
        full_name = row.xpath('//td[2]/text()').get()
        
        print(img, full_name)
3/32:
for person in persons:
    img = person.xpath('//div[@class="col-sm-5"]/div/img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//div[@class="col-sm-7"]/table/tbody')
    for row in details:
        full_name = row.xpath('//td[2]/text()').get()
        
        print(img, full_name)
3/33:
for person in persons:
    img = person.xpath('//div[@class="col-sm-5"]/div/img[@class="img-responsive"]/@src/text()').get()
    details = person.xpath('//div[@class="col-sm-7"]/table/tbody')
    print(img, details)
3/34:
for person in persons:
    img = person.xpath('//div[@class="col-sm-5"]/div/img/@src/text()').get()
    details = person.xpath('//div[@class="col-sm-7"]/table/tbody')
    print(img, details)
 4/4: from requests import fetch
 4/5: fetch()
3/35:
for person in persons:
    img = person.xpath('//div[@class="col-sm-5"]/div/img/@src').get()
    details = person.xpath('//div[@class="col-sm-7"]/table/tbody')
    print(img, details)
3/36:
for person in persons:
    img = person.xpath('//div[@class="col-sm-5"]/div/img[@class="img-responsive"]/@src').get()
    details = person.xpath('//div[@class="col-sm-7"]/table/tbody')
    for row in details:
        full_name = row.xpath('//td[2]/text()').get()
        
        print(img, full_name)
3/37: persons = response.xpath('//div[@id="divMainBody"]/div/div/div')
3/38: len(persons)
3/39: persons
3/40: persons = response.xpath('//div[@id="divMainBody"]/div/div/div/div[@class="row no-gutter"]')
3/41: len(persons)
3/42: persons = response.xpath('//div[@id="divMainBody"]/div/div/div')
3/43:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    print(details)
3/44:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    for row in details:
        img = row.xpath('//img/@src').get()
        print(img)
3/45:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    for row in details:
        img = row.xpath('//img[@class="img-responsive"]/@src').get()
        print(img)
3/46: len(persons)
3/47:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    for row in details:
        print(row)
3/48:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    i = 0
    for row in details:
        print(i, row)
        i += 1
3/49:
for person in persons:
    print(person)
3/50:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"')
    if details:
        print(details)
3/51:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    if details:
        print(details)
3/52:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
        if details is not None:
            print(details)
3/53:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    if details is not None:
        print(details)
3/54:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    i = 0
    if details is not None:
        print(i, details)
        i += 1
3/55:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    i = 0
    if details is not None:
        print(i, details, sep='\n')
        i += 1
3/56:
i=0
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    if details is not None:
        print(i, details, sep='\n')
        i += 1
3/57:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    if details is not None:
        i=0
        for row in details:
            print(i, row, sep='\n')
            i += 1
3/58:
i=0
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')[i]
    if details is not None:
        for row in details:
            print(row, sep='\n')
        i+=1
3/59:
i=1
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"][i]')
    if details is not None:
        for row in details:
            print(row, sep='\n')
        i+=1
3/60:
i=1
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"][i]')
    if details is not None:
        print(details, sep='\n')
        i+=1
3/61:
i=1
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"][i]')
    if details is not None:
        print(i, details, sep='\n')
        i+=1
3/62:
i=1
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"][i]')
    if details is not None:
        print(i, details)
        i+=1
3/63:
i=1
for person in persons:
    img = person.xpath('//div[@class="row no-gutter"][i]/div/div/img/@src')
    if img is not None:
        print(i, img)
        i+=1
3/64:
i=1
for person in persons:
    image = person.xpath('//div[@class="row no-gutter"][i]/div/div/img/@src')
    print(i, img)
    i+=1
3/65:
i=1
for person in persons:
    image = person.xpath('//div[@class="row no-gutter"][i]/div/div/img/@src').get()
    print(i, img)
    i+=1
3/66:
i=1
for person in persons:
    image = person.xpath('//div[@class="row no-gutter"][i]/div/div/img/@src').get()
    print(i, image)
    i+=1
3/67:
i=1
for person in persons:
    image = person.xpath('//img[i]/@src').get()
    print(i, image)
    i+=1
3/68: persons
3/69:
i=1
for person in persons:
    image = person.xpath('//div[@class="row no-gutter][i]').get()
    print(i, image)
    i+=1
3/70:
i=1
for person in persons:
    image = person.xpath('//div[@class="row no-gutter"][i]').get()
    print(i, image)
    i+=1
3/71:
i=1
for person in persons:
    image = person.xpath('//div[@class="row no-gutter"][i]')
    print(i, image)
    i+=1
3/72:
i=1
for person in persons:
    image = person.xpath('//div[@class="row no-gutter"][i]')
    details = person.xpath('//table[i]/tbody')
    print(i, image, details)
    i+=1
3/73: persons
3/74:
i=1
for person in persons:
    image = person.xpath('//div[i]')
    details = person.xpath('//table[i]/tbody')
    print(i, image, details)
    i+=1
3/75:
i=1
for person in persons:
    image = person.xpath('//div[i]').get()
    details = person.xpath('//table[i]/tbody')
    print(i, image, details)
    i+=1
3/76:
i=1
for person in persons:
    image = person.xpath('//div[i]').get()
    details = person.xpath('//table[i]/tbody').get()
    print(i, image, details)
    i+=1
3/77: view(response)
3/78: response
3/79:
i=1
for person in persons:
    image = person.xpath('//div[i]').get()
    details = person.xpath('//table[i]/tbody').getall()
    print(i, image, details)
    i+=1
3/80: persons = response.xpath('//div[@id="divMainBody"]/div/div/div').getall()
3/81: persons
3/82:
for person in persons:
    print(person)
3/83: len(persons)
3/84:
for person in persons:
    img = person.xpath('//img/@src').get()
    print(img)
3/85:
for person in persons:
    img = person.xpath('//img/@src')
    print(img)
3/86:
for person in persons:
    #img = person.xpath('//img/@src')
    print(person)
3/87:
for person in persons:
    details = person.xpath('//div[@class="row no-gutter"]')
    print(details)
3/88: persons = response.xpath('//div[@id="divMainBody"]/div/div/div')
3/89: len(persons)
3/90:
for person in persons:
    details = person.xpath('.//div[@class="row no-gutter"]')
    print(details)
3/91:
for person in persons:
    details = person.xpath('.//div[@class="row no-gutter"]/div/div/img')
    print(details)
3/92:
for person in persons:
    details = person.xpath('.//div[@class="row no-gutter"]/div/div/img').get()
    print(details)
3/93: persons
3/94:
for person in persons:
    details = person.xpath('.//div[@class="row no-gutter"]/div/div/img/@src').get()
    print(details)
3/95: images = response.xpath('//img[@class="img-responsive"]/@src').getall()
3/96: images
3/97: names = response.xpath('//tbody/tr[1]/td[2]/text()').getall()
3/98: names
3/99: names = response.xpath('//tbody/tr/td[2]/text()').getall()
3/100: names
3/101: names = response.xpath('//div[@class="col-sm-7"]/table/tbody/tr[1]/td[2]/text()').getall()
3/102: names
3/103: names = response.xpath('//table/tbody/tr[1]/td[2]/text()').getall()
3/104: names
3/105: names = response.xpath('//table/tbody/tr[1]/td[2]/span/text()').getall()
3/106: names
3/107: names = response.xpath('//tbody/tr[1]/td[2]/span/text()').getall()
3/108: names
3/109: genders = response.xpath('//tbody/tr[2]/td[2]/text()').getall()
3/110: genders
3/111: races = response.xpath('//tbody/tr[2]/td[5]/text()').getall()
3/112: races
3/113: dobs = response.xpath('//tbody/tr[3]/td[2]/text()').getall()
3/114: dobs
3/115: ages = response.xpath('//tbody/tr[3]/td[5]/text()').getall()
3/116: ages
3/117: heights = response.xpath('//tbody/tr[4]/td[2]/text()').getall()
3/118: heights
3/119: weights = response.xpath('//tbody/tr[4]/td[5]/text()').getall()
3/120: weights
3/121: hairs = response.xpath('//tbody/tr[5]/td[2]/text()').getall()
3/122: hairs
3/123: eyes = response.xpath('//tbody/tr[5]/td[5]/text()').getall()
3/124: eyes
3/125: cases = response.xpath('//tbody/tr[7]/td/text()').getall()
3/126: cases
3/127: notes = response.xpath('//tbody/tr[8]/td/div[1]/text()').getall()
3/128: notes
3/129: notes2 = response.xpath('//tbody/tr[8]/td/div[2]/text()').getall()
3/130: notes2
3/131: len(cases)
3/132: len(eyes)
3/133: testing = response.xpath('//tbody/tr/td/div[@xstyle="font-size:16px;color:#23539F;font-weight:bold;line-height: 1.2"]/text()').getall()
3/134: testing
3/135: len(testing)
3/136: notes_1 = response.xpath('//tbody/tr/td/div[@xstyle="font-size:16px;color:#23539F;font-weight:bold;line-height: 1.2"]/text()').getall()
3/137: notes_2 = response.xpath('//tbody/tr/td/div[@xstyle="color:#aaaaaa;font-size:10px;line-height: 1.2"]/text()').getall()
3/138: notes_2
3/139: len(notes_1)
3/140: len(notes_2)
3/141: len(eyes)
3/142: notes_1 = response.xpath('//tbody/tr/td/div[@xstyle="font-size:16px;color:#23539F;font-weight:bold;line-height: 1.2"]/text()').extract()
3/143: notes_1
3/144: len(notes_1)
3/145:
for item in notes_1:
    print(itme)
3/146:
for item in notes_1:
    print(item)
 5/1: from scrapy.selector import Selector
 5/2: %paste
 6/1: from scrapy.selector import Selector
 6/2: %paste
 7/1: fetch("http://www.missingandunsolved.com/hawaii/")
 7/2: response
 7/3: response.text
 7/4: response.xpath('//h1/a/text()').extract_first()
 7/5: source_head = response.xpath('//html/head/title/text()').extract_first()
 7/6: source_head
 7/7:
with open('nothing.txt', 'w') as fo:
    fo.write(response.text)
 8/1: from scrapy.selector import Selector
 8/2: %paste
 7/8: response.xpath('//ul[@class="display-posts-listing"])
 7/9: response.xpath('//ul[@class="display-posts-listing"]')
7/10: response.xpath('//li[@class="listing-item"]')
7/11: listing = response.xpath('//li[@class="listing-item"]')
7/12:
for item in listing:
    print(item.xpath('//a[@class=""]/img/@src')).get()
7/13:
for item in listing:
    print(listing.xpath('//a[@class=""]/img/@src')).get()
7/14:
for item in listing:
    print(listing.xpath('//a[@class=""]/img/@src')).extrace()
7/15: item = listing.xpath('//a[@class=""]/img/@src').extract()
7/16: item
7/17: item = listing.xpath('//a[@class="image"]/img/@src').extract()
7/18: item
7/19: len(item)
7/20: item = listing.xpath('//a[@class="image"]/img/@src')
7/21: len(item)
7/22: len(listing)
7/23: item = listing.xpath('.//a[@class="image"]/img/@src').extract()
7/24: len(item)
7/25: item
7/26: item = ""
7/27: del(item)
7/28: item
7/29:
for item in listing:
    url = item.xpath('//a[@class="image"]/img/@src').get()
    print(url)
7/30:
for item in enumerate(listing):
    url = item.xpath('//a[@class="image"]/img/@src').get()
    print(url)
7/31:
for item in listing:
    url = item.xpath('img/@src').get()
    print(url)
7/32:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    print(url)
7/33:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').get()
    print(fname)
7/34:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)')
    print(fname)
7/35:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\(')
    print(fname)
7/36:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(').get().strip().title()
    print(fname)
7/37:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(').extract_first().strip().title()
    print(fname)
7/38:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
    print(fname)
7/39:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
    notes = item.xpath('span[@class="excerpt"]/text()').get()
    print(notes)
7/40:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
    age = item.xpath('span[@class="excerpt"]/text()').re(r'Age.*:\s*(\d*),')
    print(age)
7/41:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
    age = item.xpath('span[@class="excerpt"]/text()').re(r'Age.*:\s*(\d*),')[0]
    print(age)
7/42:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
    age = item.xpath('span[@class="excerpt"]/text()').re(r'Age.*:\s*(\d*),')[0]
    missing_since = item.xpath('span[@class="excerpt"]/text()').re(r'(\d{1,2}/\d{1,2}/\d{4})')[0]
    print(missing_since)
7/43:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
    age = item.xpath('span[@class="excerpt"]/text()').re(r'Age.*:\s*(\d*),')[0]
    missing_since = item.xpath('span[@class="excerpt"]/text()').re(r'(\d{1,2}/\d{1,2}/\d{4})')[0]
    notes = item.xpath('span[@class="excerpt"]/text()').get().strip()
    print(notes)
7/44:
for item in listing:
    url = item.xpath('a[@class="image"]/img/@src').get()
    fname = item.xpath('a[@class="title"]/text()').re(r'Missing:\s*(.*)\s*\(')[0].strip().title()
    age = item.xpath('span[@class="excerpt"]/text()').re(r'Age.*:\s*(\d*),')[0]
    missing_since = item.xpath('span[@class="excerpt"]/text()').re(r'(\d{1,2}/\d{1,2}/\d{4})')[0]
    notes = item.xpath('span[@class="excerpt"]/text()').get().strip().title()
    print(notes)
7/45: fb_listing = response.xpath('//div[@class="cff-posts-wrap"]')
7/46: len(fb_listing)
7/47: fb_listing = response.xpath('//div[@id="cff"]')
7/48: len(fb_listing)
7/49: fb_listing
7/50: fb_listing = response.xpath('//div[@data-page-id="HawaiiLostNMissing"]')
7/51: len(fb_listing)
7/52: fb_listing = response.xpath('//p[@class="cff-post-text"]')
7/53: len(fb_listing)
7/54: fb_listing = response.xpath('//div[@class="cff-text-wrapper"]')
7/55: len(fb_listing)
7/56:
for item in fb_listing:
    note = item.xpath('//span[@class="cff-text"]').get()
7/57:
for item in fb_listing:
    note = item.xpath('//span[@class="cff-text"]').get()
    print(note)
7/58:
for item in fb_listing:
    note = item.xpath('//span[@class="cff-text"]/text()').get()
    print(note)
7/59:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-text"]/span[descendant-or-self::text()]').get()
    print(note)
7/60:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-text"]/span[@class="cff-text"]')
    print(note.get())
7/61:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]/span[@class="cff-text"]')
    print(note)
7/62:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]/span[@class="cff-text"]')
    print(note.get())
7/63:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]/span[@class="cff-text"]/text()')
    print(note.get())
7/64:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]/span[@class="cff-text"]/text()')
    if note.get() is str:
        print(note.get())
    else:
        print("oh")
7/65:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]/span[@class="cff-text"]/text()')
    if type(note.get()) is str:
        print(note.get())
    else:
        print("oh")
7/66:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]/span[@class="cff-text"]')
    if type(note.xpath('text()').get()) is str:
        print(note.get())
    else:
        print("oh")
7/67:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]/span[@class="cff-text"]')
    if type(note.xpath('text()').get()) is str:
        print(note.xpath('text()').get())
    else:
        print("oh")
7/68:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]')
    n1 = note.xpath('//span[@class="cff-text"]')
    if type(n1.xpath('text()').get()) is str:
        print(n1.xpath('text()').get())
    else:
        print("oh")
7/69:
for item in fb_listing:
    note = item.xpath('//p[@class="cff-post-text"]')
    n1 = note.xpath('//span[@class="cff-text"]')
    if type(n1.xpath('text()').get()) is str:
        print(n1.xpath('text()').get())
    else:
        print("oh")
7/70: fb_listing = response.xpath('//p[@class="cff-post-text"]')
7/71: len(fb_listing)
7/72:
for item in fb_listing:
    n1 = item.xpath('//span[@class="cff-text"]')
    print(n1.text())
7/73:
for item in fb_listing:
    n1 = item.xpath('//span[@class="cff-text"]')
    print(n1.xpath('text()'))
7/74:
for item in fb_listing:
    n1 = item.xpath('//span[@class="cff-text"]')
    print(n1)
7/75:
for item in fb_listing:
    n1 = item.xpath('//span[@class="cff-text"]/a/text()').get()
    print(n1)
7/76:
for item in fb_listing:
    n1 = item.xpath('//span[@class="cff-text"]/text()').get()
    print(n1)
7/77:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/text()').get()
    print(n1)
7/78:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/text()').get()
    if type(n1) is str:
        print(n1)
    else:
        print('oh')
7/79:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/text()').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/80:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/a[descendant-or-self::text()]').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/81:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/text()').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/82:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/node()').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/83:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/node()').re('.*[>]*(.*)')
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/84:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/child::node()').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/85:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/text()').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/86:
for item in fb_listing:
    n1 = item.xpath('string(span[@class="cff-text"]/text())').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/87:
for item in fb_listing:
    n1 = item.xpath('span[@class="cff-text"]/text()').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/88:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').get()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/89:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    if type(n1) is str:
        print(n1.strip())
    else:
        print('oh')
7/90:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    if type(n1) is str:
        print(n1.strip())
    else:
        print(n1)
7/91:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    if type(n1) is str:
        print(n1.strip())
    else:
        print(len(n1), n1)
7/92:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    if type(n1) is str:
        print(n1.strip())
    else:
        print(",".join(n1))
7/93:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    if type(n1) is str:
        print(n1.strip())
    else:
        print(" ".join(n1))
7/94:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    if type(n1) is str:
        print(n1.strip())
    else:
        n2 = [x.strip() for x in n1]
        print(" ".join(n2), sep='\n')
7/95:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    if type(n1) is str:
        print(n1.strip())
    else:
        n2 = [x.strip() for x in n1]
        print(" ".join(n2), sep='\n\n')
7/96:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    print(" ".join(n2), sep='\n')
7/97:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    n3 = " ".join(n2)
7/98: import re
7/99:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        print(x[0])
7/100:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        print(x)
7/101:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),")
            name = n.match(x).group()
            print(name)
7/102:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),")
            name = n.match(x).group(0)
            print(name)
7/103:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),")
            name = n.match(x).group(1)
            print(name)
7/104:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            print(name, age)
7/105:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            print(name, age)
7/106:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
7/107:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
7/108:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!" | "^Our condolences" | "^Media", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
        elif skip:
            print('skip')
        else:
            print('ok')
7/109:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news! | ^Our condolences | ^Media", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
        elif skip:
            print('skip')
        else:
            print('ok')
7/110:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("Great news! | Our condolences | Media", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
        elif skip:
            print('skip')
        else:
            print('ok')
7/111:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("Great news! | Our condolences | Media", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
        #elif skip:
            #print('skip')
        else:
            print('ok')
7/112:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("Great news! | Our condolences | Media", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        #elif skip:
            #print('skip')
        else:
            print('ok')
7/113:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("Great news! | Our condolences | Media", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        #elif skip:
            #print('skip')
        else:
            continue
7/114: s = 'hello'
7/115: type(s) is str
7/116: type(s) is list
7/117: type(s) is obj
7/118: type(s) is object
7/119: type(s).__name__ == 'str'
7/120:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip:
            print('skip')
            continue
        else:
            continue
7/121: len(fb_listing)
7/122:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            n = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = n.match(x).group(1)
            age = n.match(x).group(2)
            notes = n.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            continue
7/123:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            c1 = re.compile("^(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
7/124:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            c1 = re.compile("^(?.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
7/125:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            c1 = re.compile("^(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
7/126:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
7/127:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        skip4 = not rr
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3 or skip4:
            print('skip')
            continue
        else:
            c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
7/128:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
7/129:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            #c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
            #name = c1.match(x).group(1)
            #age = c1.match(x).group(2)
            #notes = c1.match(x).group(3)
            #print(name, age, notes, sep=';')
            print(x)
            continue
7/130:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        elif not (rr and skip and skip2 and skip3):
            continue
        else:
            #c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
            #name = c1.match(x).group(1)
            #age = c1.match(x).group(2)
            #notes = c1.match(x).group(3)
            #print(name, age, notes, sep=';')
            print(x)
            continue
7/131:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
7/132:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            try:
                c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
                name = c1.match(x).group(1)
                age = c1.match(x).group(2)
                notes = c1.match(x).group(3)
            except:
                print('skip2')
            else:
                print(name, age, notes, sep=';')
            finally:
                continue
7/133:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            #continue
        elif skip or skip2 or skip3:
            print('skip')
            #continue
        else:
            try:
                c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
                name = c1.match(x).group(1)
                age = c1.match(x).group(2)
                notes = c1.match(x).group(3)
            except:
                print('skip2')
            else:
                print(name, age, notes, sep=';')
        continue
7/134:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            try:
                c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
                name = c1.match(x).group(1)
                age = c1.match(x).group(2)
                notes = c1.match(x).group(3)
            except:
                print('skip2')
            else:
                print(name, age, notes, sep=';')
                continue
7/135:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            try:
                c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
                name = c1.match(x).group(1)
                age = c1.match(x).group(2)
                notes = c1.match(x).group(3)
            except:
                continue
            else:
                print(name, age, notes, sep=';')
                continue
            finally:
                print('skip2')
7/136:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/text()').getall()
    n2 = [x.strip() for x in n1]
    for x in n2:
        rr = re.search("^#.*Missing\s*", x)
        skip = re.search("^Great news!", x)
        skip2 = re.search("^Our condolences", x)
        skip3 = re.search("^Media", x)
        if rr:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
            continue
        elif skip or skip2 or skip3:
            print('skip')
            continue
        else:
            try:
                c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
                name = c1.match(x).group(1)
                age = c1.match(x).group(2)
                notes = c1.match(x).group(3)
            except:
                continue
            else:
                print(name, age, notes, sep=';')
                continue
7/137:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n2 = [x.strip() for x in n1]
    print(n2[0])
7/138:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    #print(n1_list[0])
    re1 = re.search("^#.*Missing", n1_list[0])
    re2 = re.search("^<a.*#StillMissing", n1_list[0])
    if re1:
        c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    elif re2:
        c1 = re.compile("^<a.*</a>\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    else:
        print(n1_list[0])
7/139:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#StillMissing", x)
    if re1:
        c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    elif re2:
        c1 = re.compile("^<a.*</a>\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    else:
        print(x)
7/140:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#StillMissing", x)
    if re1:
        c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    elif re2:
        c1 = re.compile("^<a.*a>\s*(.*),\s*(\d*),\s*(.*)")
        c2 = re.compile("^<a.*a>\s*(.*?),\s*(.*)")
        if c1:
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
        elif c2:
            name = c2.match(x).group(1)
            notes = c2.match(x).group(2)
            print(name, notes, sep=';')
    else:
        print(x)
7/141:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#StillMissing", x)
    if re1:
        c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    elif re2:
        c1 = re.compile("^<a.*a>(.*),\s*(\d*),\s*(.*)")
        c2 = re.compile("^<a.*a>(.*?),\s*(.*)")
        if c1:
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
        elif c2:
            name = c2.match(x).group(1)
            notes = c2.match(x).group(2)
            print(name, notes, sep=';')
    else:
        print(x)
7/142:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    elif re2:
        c1 = re.compile("^<a.*#.*Missing.*a>(.*),\s*(\d*),\s*(.*)")
        c2 = re.compile("^<a.*#.*Missing.*a>(.*?),\s*(.*)")
        if c1:
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
        elif c2:
            name = c2.match(x).group(1)
            notes = c2.match(x).group(2)
            print(name, notes, sep=';')
    else:
        print(x)
7/143:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    elif re2:
        c1 = re.compile("^<a.*#.*Missing</a>(.*),\s*(\d*),\s*(.*)")
        c2 = re.compile("^<a.*#.*Missing</a>(.*?),\s*(.*)")
        if c1:
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
        elif c2:
            name = c2.match(x).group(1)
            notes = c2.match(x).group(2)
            print(name, notes, sep=';')
    else:
        print(x)
7/144:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
        name = c1.match(x).group(1)
        age = c1.match(x).group(2)
        notes = c1.match(x).group(3)
        print(name, age, notes, sep=';')
    elif re2:
        if re.compile("^<a.*#.*Missing</a>(.*),\s*(\d*),\s*(.*)"):
            c1 = re.compile("^<a.*#.*Missing</a>(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
            print(name, age, notes, sep=';')
        else:
            c2 = re.compile("^<a.*#.*Missing</a>(.*),\s*(.*)")
            name = c2.match(x).group(1)
            notes = c2.match(x).group(2)
            print(name, notes, sep=';')
    else:
        print(x)
7/145:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print(x)
        else:
            print(name, age, notes, sep=';')
    elif re2:
        try:
            c1 = re.compile("^<a.*#.*Missing</a>(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print(x)
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/146:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1)
        else:
            print(name, age, notes, sep=';')
    elif re2:
        try:
            c1 = re.compile("^<a.*#.*Missing</a>(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re2')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/147:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        try:
            c1 = re.compile("^<a.*#.*Missing</a>(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re2')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/148:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        try:
            c1 = re.compile(r"^<a.*#.*Missing</a>(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re2')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/149:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        try:
            c1 = re.compile(r"^<a.*#.*Missing</a>(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re2')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/150:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        try:
            c1 = re.compile("(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re2')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/151:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        try:
            c1 = re.compile("a>(.*?),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re2')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/152:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            print('within re2')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/153:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            print('re2', x2)
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/154:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),.*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            print('re2', x2)
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/155:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),.*?(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            print('re2', x2)
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/156:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*?.*?(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            print('re2', x2)
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/157:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            print('re2', x2)
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/158:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            c1 = re.compile("(.*?),(.*)")
            name = c1.match(x2).group(1)
            notes = c1.match(x2).group(2)
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/159:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            c1 = re.compile("(.*?),(.*)")
            name = c1.match(x2).group(1)
            notes = c1.match(x2).group(2)
            print(name, notes, sep=';')
        else:
            print(name, age, notes, sep=';')
    else:
        print(x)
7/160:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[1:])
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            try:
                c1 = re.compile("(.*?),(.*)")
                name = c1.match(x2).group(1)
                age = 0
                notes = c1.match(x2).group(2)
            except:
                print(x2)
            else:
                print(name, notes, sep=';')
                notes_2 = " ".join(n1_list[2:])
        else:
            print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[2:])
    else:
        print(x)
        name, age, notes, notes_2 = ("", 0, "", x)
7/161:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            print('within re1')
        else:
            print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[1:])
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            try:
                c1 = re.compile("(.*?),(.*)")
                name = c1.match(x2).group(1)
                age = 0
                notes = c1.match(x2).group(2)
            except:
                print(x2)
            else:
                print(name, notes, sep=';')
                notes_2 = " ".join(n1_list[2:])
        else:
            print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[2:])
    else:
        print(x)
        name, age, notes, notes_2 = ("", 0, "", " ".join(n1_list))
7/162:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search("^#.*Missing", x)
    re2 = re.search("^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile("^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            #print('within re1')
            name, age, notes, notes_2 = ("", 0, "", " ".join(n1_list))
        else:
            #print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[1:])
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile("(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            try:
                c1 = re.compile("(.*?),(.*)")
                name = c1.match(x2).group(1)
                age = 0
                notes = c1.match(x2).group(2)
            except:
                #print(x2)
                name, age, notes, notes_2 = ("", 0, "", " ".join(n1_list))
            else:
                #print(name, notes, sep=';')
                notes_2 = " ".join(n1_list[2:])
        else:
            #print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[2:])
    else:
        #print(x)
        name, age, notes, notes_2 = ("", 0, "", " ".join(n1_list))
7/163:
for item in fb_listing:
    n1 = item.xpath('.//span[@class="cff-text"]/node()').getall()
    n1_list = [x.strip() for x in n1]
    x = n1_list[0]
    re1 = re.search(r"^#.*Missing", x)
    re2 = re.search(r"^<a.*#.*Missing", x)
    if re1:
        try:
            c1 = re.compile(r"^#.*Missing\s*(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x).group(1)
            age = c1.match(x).group(2)
            notes = c1.match(x).group(3)
        except:
            #print('within re1')
            name, age, notes, notes_2 = ("", 0, "", " ".join(n1_list))
        else:
            print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[1:])
    elif re2:
        x2 = n1_list[1]
        try:
            c1 = re.compile(r"(.*),\s*(\d*),\s*(.*)")
            name = c1.match(x2).group(1)
            age = c1.match(x2).group(2)
            notes = c1.match(x2).group(3)
        except:
            try:
                c1 = re.compile(r"(.*?),(.*)")
                name = c1.match(x2).group(1)
                age = 0
                notes = c1.match(x2).group(2)
            except:
                print(x2)
                name, age, notes, notes_2 = ("", 0, "", " ".join(n1_list))
            else:
                print(name, notes, sep=';')
                notes_2 = " ".join(n1_list[2:])
        else:
            print(name, age, notes, sep=';')
            notes_2 = " ".join(n1_list[2:])
    else:
        print(x)
        name, age, notes, notes_2 = ("", 0, "", " ".join(n1_list))
7/164: %history > scrapy_hist.txt
7/165: %history
7/166: %hist -o -f scrapy_history.md
   1: %history -o -g -f scrapy_history.md
