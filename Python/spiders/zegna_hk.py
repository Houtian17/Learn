"""
    Author : HuZhibin
    杰尼亚
"""

from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'zagna_hk'
    brand_name = 'zagna_hk'
    allowed_domains = ['zegna.com']
    sitemap_urls = ['https://www.zegna.com/hk-tw.sitemap.xml']
    sitemap_rules = [
        (r'[\w].+product.[\w].+', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code = response.css('span.infoProduct__button::text').get()

        price_hkd = response.css('span.pdpData__price::text').get().strip().strip('HK$').replace(',', '')
        price = {
            'hkd': float(price_hkd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])
        yield sku
