"""
    Author : HuZhibin
    品高
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import json
import requests

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'pinko_us'
    brand_name = 'pinko_us'
    allowed_domains = ['pinko.com']
    sitemap_urls = ['https://www.pinko.com/en-us/sitemap_0.xml']
    sitemap_rules = [
        (r'/zh-us/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        code = response.css('span[itemprop="productID"]::text').get()

        if code is None:
            return

        price_usd = response.css('span.price-sales::text').get().strip('$ ').replace('.', '').replace(',', '.')
        price = {
            'usd': float(price_usd)
        }

        sku = SKU(self.brand_name, '', '', code, '', '', price, '', {}, {})
        yield sku
