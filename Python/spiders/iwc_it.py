from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU
import re
import json


class SitemapTemplateSpider(SitemapSpider):
    name = 'iwc_it'
    brand_name = '万国'
    allowed_domains = ['iwc.com']
    sitemap_urls = ['https://www.iwc.com/it/en.sitemap.xml']
    sitemap_rules = [
        ('/it/en/watch-collections/', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code = response.css('h2.iwc-buying-options-reference::text').get()

        tracking_product = json.loads(response.css('button[data-tracking-product]').attrib['data-tracking-product'])
        eur = tracking_product['price']

        price = {
            'eur': float(eur)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
