"""
    Author : HuZhibin
    积家us
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'jaeger-lecoultre_us'
    brand_name = 'jaeger-lecoultre_us'
    allowed_domains = ['jaeger-lecoultre.com']
    sitemap_urls = ['https://www.jaeger-lecoultre.com/us/en/home-page/sitemap.xml']
    sitemap_rules = [
        (r'/watches/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        name = response.css('div.pdp-top__name::text').get()

        if name is None:
            return

        code = response.css('span[itemprop="sku"]::text').get()

        price_usd = response.css('span[itemprop="price"]::text').get().strip().strip('$').replace(',', '')

        try:
            price_eur = float(price_usd)
        except Exception as e:
            return

        price = {
            'usd': float(price_usd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', {}, {})

        yield sku
