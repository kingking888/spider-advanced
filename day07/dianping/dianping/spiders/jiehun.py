# -*- coding: utf-8 -*-
import scrapy


class JiehunSpider(scrapy.Spider):
    name = 'jiehun'
    # allowed_domains = ['xxx']
    start_urls = ['http://www.dianping.com/beijing/ch55/g163']

    def parse(self, response):
        all_url = response.xpath('//p[@class="title"]/a/@href').extract()
        for url in all_url:
            url = 'http:' + url
            shopid = url[29:]
            yield scrapy.Request(url=url, callback=self.parse_dianpu, meta={'shopid': shopid})

    def parse_dianpu(self, response):
        # ID
        shopid = response.meta['shopid']
        # 店名
        shopname = response.xpath('//h1[@class="shop-title"]/text()').extract_first()
        print('店名：', shopname)
        # 地址
        address = response.xpath('//span[@class="fl road-addr"]/text()').extract()[1].strip()
        print('地址：', address)
        # 电话
        phone = response.xpath('//span[@class="icon-phone"]/text()').extract_first().replace(' ', '').replace(
            '\xa0', '').replace('\n', ',')
        print('电话：', phone)
        # 精选套餐列表页
        select_package_url = 'http://www.dianping.com' + \
                             response.xpath('//div[@id="J_boxPack"]//div[@class="hd"]//a/@href').extract()[0]
        print('精选套餐：', select_package_url)
        # 会员相册列表页
        photos_package_url = 'http://www.dianping.com' + \
                             response.xpath('//*[@id="J_boxAlbum"]/div[1]/a/@href').extract()[0]
        print('会员相册：', photos_package_url)
        # 官方案例列表页
        detail_official_case_url = 'http://www.dianping.com' + response.xpath(
            '//div[@id="J_boxCases"]//div[@class="hd"]//a/@href').extract_first()
        print('官方案例url：', detail_official_case_url)
        # 官方案例详情页
        url = 'http://www.dianping.com/wed/ajax/shopweb/case_cases'
        for page in range(1, 5):
            form_data = {
                'fallPage': str(page),
                'productCategoryId': '0',
                'tagValues': '0',
                'shopId': str(shopid),
                'page': '1',
            }
            yield scrapy.FormRequest(url=url, formdata=form_data, callback=self.parse_anli,
                                     meta={'shopname': shopname, 'page': page})

    def parse_anli(self, response):
        shopname = response.meta['shopname']
        page = response.meta['page']
        print('==========' + shopname + '第%s页官方案例' % page + '==========')
        print(response.text[:100])
