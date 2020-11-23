"""
    Author : HuZhibin
    宝格丽
"""
import warnings

import scrapy
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider, Spider
from scrapy.utils.deprecate import method_is_overridden

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'bulgari_us'
    brand_name = 'bulgari_us'
    allowed_domains = ['bulgari.com']
    sitemap_urls = ['https://www.bulgari.com/en-us/sitemap_0.xml']
    sitemap_rules = [
        (r'/en-us/', 'parse_sku'),
    ]

    custom_settings = {
        'COOKIES_ENABLED': True,
        'DUPEFILTER_DEBUG': True,
    }

    def start_requests(self):
        for url in self.sitemap_urls:
            yield Request(url, self._parse_sitemap, dont_filter=True)

    def parse_sku(self, response: Response):
        attrs = []

        code = response.css('span.product-id::text').get()
        price = {}
        price_usd = response.css('span.value').attrib['content']
        if price_usd:
            price_usd = price_usd.strip('$').replace(',', '').strip()
            price = {
                'usd': float(price_usd),
            }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], attrs)
        yield sku
