"""
    Author : HuZhibin
    芬迪
"""
from json import JSONDecodeError

from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import json
import requests

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'fendi_it'
    brand_name = 'fendi_it'
    allowed_domains = ['fendi.com']
    sitemap_urls = ['https://www.fendi.com/sitemap.xml']
    sitemap_follow = ['xml']

    sitemap_rules = [
        (r'/it/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        code = response.css('span[itemprop="productID"]::text').get()
        if code is None:
            print('当前地址应该不是详情页：', response.url)
            return

        price_eur = response.css('meta[itemprop="price"]').attrib['content']

        price = {
            'eur': price_eur,
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
