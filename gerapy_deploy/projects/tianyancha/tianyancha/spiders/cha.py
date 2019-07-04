# -*- coding: utf-8 -*-
import time
import scrapy
from ..items import TianyanchaItem


class ChaSpider(scrapy.Spider):
    name = 'cha'
    # allowed_domains = ['https://www.tianyancha.com/']
    start_urls = ['https://www.tianyancha.com/search']

    def parse(self, response):
        all_strid = response.xpath('//*[@id="search-filter"]/div[2]/div/div[2]/div[1]/a/@href').extract()
        for strid in all_strid:
            for page in range(1, 6):
                url = 'https://www.tianyancha.com/search/p' + str(page) + '?' + strid[34:].strip()
                yield scrapy.Request(url, callback=self.parse_list)

    def parse_list(self, response):
        time.sleep(2)
        all_link = response.xpath('//*[@id="web-content"]/div/div[1]/div[2]/div[2]/div/div')
        for link in all_link:
            name = link.xpath(".//img/@alt").extract_first()
            href = link.xpath(".//a/@href").extract_first()
            yield scrapy.Request(url=href, callback=self.parse_detail, meta={'name': name, 'href': href})

    def parse_detail(self, response):
        item = TianyanchaItem()
        item['name'] = response.meta['name']
        item['href'] = response.meta['href']
        item['addr'] = response.xpath(
            '//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[2]/div[2]/div/div/text()').extract_first('暂无信息')
        item['call'] = response.xpath(
            '//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[1]/div[1]/span[2]/text()').extract_first('暂无信息')
        item['mail'] = response.xpath(
            '//*[@id="company_web_top"]/div[2]/div[3]/div[3]/div[1]/div[2]/span[2]/text()').extract_first('暂无信息')
        yield item
