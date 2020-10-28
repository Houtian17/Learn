"""
    Author : HuZhibin
    积家hk
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'jaeger-lecoultre_hk'
    brand_name = 'jaeger-lecoultre_hk'
    allowed_domains = ['jaeger-lecoultre.com']
    sitemap_urls = ['https://www.jaeger-lecoultre.com/hk/en/home-page/sitemap.xml']
    sitemap_rules = [
        (r'/watches/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        name = response.css('div.pdp-top__name::text').get()

        if name is None:
            return

        code = response.css('span[itemprop="sku"]::text').get()

        price_hkd = response.css('span[itemprop="price"]::text').get().strip().strip('HK$').replace(',', '')

        try:
            price_eur = float(price_hkd)
        except Exception as e:
            return

        price = {
            'hkd': float(price_hkd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', {}, {})

        yield sku
