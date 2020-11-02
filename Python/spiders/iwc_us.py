from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU
import re
import json


class SitemapTemplateSpider(SitemapSpider):
    name = 'iwc_us'
    brand_name = '万国'
    allowed_domains = ['iwc.com']
    sitemap_urls = ['https://www.iwc.com/us/en.sitemap.xml']
    sitemap_rules = [
        ('/us/en/watch-collections/', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code = response.css('h2.iwc-buying-options-reference::text').get()

        tracking_product = json.loads(response.css('button[data-tracking-product]').attrib['data-tracking-product'])
        usd = tracking_product['price']

        price = {
            'usd': float(usd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
