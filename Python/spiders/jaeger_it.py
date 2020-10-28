"""
    Author : HuZhibin
    积家it
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'jaeger-lecoultre_it'
    brand_name = 'jaeger-lecoultre_it'
    allowed_domains = ['jaeger-lecoultre.com']
    sitemap_urls = ['https://www.jaeger-lecoultre.com/eu/it/home-page/sitemap.xml']
    sitemap_rules = [
        (r'/watches/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        name = response.css('div.pdp-top__name::text').get()

        if name is None:
            return

        code = response.css('span[itemprop="sku"]::text').get()

        price_eur = response.css('div[data-priceval]').attrib['data-priceval']

        if price_eur is None:
            return

        try:
            price_eur = float(price_eur)
        except Exception as e:
            return

        price = {
            'eur': float(price_eur)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', {}, {})

        yield sku
