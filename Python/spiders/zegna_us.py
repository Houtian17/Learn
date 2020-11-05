"""
    Author : HuZhibin
    杰尼亚
"""

from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'zagna_us'
    brand_name = 'zagna_us'
    allowed_domains = ['zegna.com']
    sitemap_urls = ['https://www.zegna.com/us-es.sitemap.xml']
    sitemap_rules = [
        (r'[\w].+product.[\w].+', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code = response.css('span.infoProduct__button::text').get()

        price_usd = response.css('span.pdpData__price::text').get().strip().strip('$ ').replace(',', '')
        price = {
            'usd': float(price_usd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])
        yield sku
