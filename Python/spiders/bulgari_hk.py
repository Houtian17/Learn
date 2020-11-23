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
    name = 'bulgari_hk'
    brand_name = 'bulgari_hk'
    allowed_domains = ['bulgari.com']
    sitemap_urls = ['https://www.bulgari.com/zh-hk/sitemap_0.xml']
    sitemap_rules = [
        (r'/zh-hk/', 'parse_sku'),
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
        price_hkd = response.css('span.value').attrib['content']
        if price_hkd:
            price_hkd = price_hkd.strip('HKD$').replace(',', '').strip()
            price = {
                'hkd': float(price_hkd),
            }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], attrs)
        yield sku
