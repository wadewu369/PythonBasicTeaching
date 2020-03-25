import scrapy
from constellation.items import ConstellationItem
import time
import re

today_time = time.strftime("%Y-%m-%d", time.localtime())


class constellationSpider(scrapy.Spider):
    name = 'constellation'
    allowed_domains = ['http://astro.click108.com.tw/']
    start_urls = ['http://astro.click108.com.tw/daily_0.php?iAstro=0&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_1.php?iAstro=1&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_2.php?iAstro=2&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_3.php?iAstro=3&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_4.php?iAstro=4&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_5.php?iAstro=5&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_6.php?iAstro=6&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_7.php?iAstro=7&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_8.php?iAstro=8&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_9.php?iAstro=9&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_10.php?iAstro=10&iAcDay=%s' % today_time,
                  'http://astro.click108.com.tw/daily_11.php?iAstro=11&iAcDay=%s' % today_time
                  ]

    def parse(self, response):
        item = ConstellationItem()
        target = response.css(".TODAY_CONTENT")

        dr = re.compile(r'<[^>]+>', re.S)
        # dd = dr.sub('')

        for tag in target:
            item['name'] = tag.css("h3::text")[0].get()
            item['OverallFortuneTitle'] = tag.css('span::text')[0].get()
            item['LoveFortuneTitle'] = tag.css('span::text')[1].get()
            item['CareerFortuneTitle'] = tag.css('span::text')[2].get()
            item['WealthFortuneTitle'] = tag.css('span::text')[3].get()
            item['OverallFortuneContent'] = tag.css('p::text')[1].get()
            item['LoveFortuneContent'] = tag.css('p::text')[3].get()

            CareerFortuneContent = tag.css('p')[5].get()
            getCareerFortuneContent = dr.sub('', CareerFortuneContent)
            WealthFortuneContent = tag.css('p')[7].get()
            getWealthFortuneContent = dr.sub('', WealthFortuneContent)
            item['CareerFortuneContent'] = getCareerFortuneContent
            item['WealthFortuneContent'] = getWealthFortuneContent
            # item['CareerFortuneContent'] = tag.css('p')[5].extract()
            # item['WealthFortuneContent'] = tag.css('p')[7].get()
            yield item
