"""
    Author : HuZhibin
    华伦天奴
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import json
import requests

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'valentino_hk'
    brand_name = 'valentino_hk'
    allowed_domains = ['valentino.com']
    sitemap_urls = ['https://www.valentino.com/sitemap_hk_valentino.xml']
    sitemap_rules = [
        (r'[\w].+[\w]+cod[\w].+', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        code = response.css('div.itemInfo-modelfabricolor span.value::text').get()

        hkd = response.css('span.price span.value::text').get().strip('HKD ').replace(',', '')
        price = {
            'hkd': float(hkd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
