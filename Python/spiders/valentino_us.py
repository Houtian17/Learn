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
    name = 'valentino_us'
    brand_name = 'valentino_us'
    allowed_domains = ['valentino.com']
    sitemap_urls = ['https://www.valentino.com/sitemap_us_valentino.xml']
    sitemap_rules = [
        (r'[\w].+[\w]+cod[\w].+', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        code = response.css('div.itemInfo-modelfabricolor span.value::text').get()

        usd = response.css('span.price span.value::text').get().strip('$').replace(',', '')
        price = {
            'usd': float(usd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
