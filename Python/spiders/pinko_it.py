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
    name = 'pinko_it'
    brand_name = 'pinko_it'
    allowed_domains = ['pinko.com']
    sitemap_urls = ['https://www.pinko.com/it-it/sitemap_index.xml']
    sitemap_rules = [
        (r'/it-it/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        code = response.css('span[itemprop="productID"]::text').get()

        if code is None:
            return

        price_eur = response.css('span.price-sales::text').get().strip('€ ').replace('.', '').replace(',', '.')

        price = {
            'eur': float(price_eur)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], {})
        yield sku
