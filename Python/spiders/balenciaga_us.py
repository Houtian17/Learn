"""
    Author : HuZhibin
    巴黎世家
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import re

from ..libs import utils

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'balenciaga_us'
    brand_name = 'balenciaga_us'
    allowed_domains = ['balenciaga.com']
    sitemap_urls = ['https://www.balenciaga.com/sitemap_us_balenciaga.xml']
    sitemap_rules = [
        (r'[\w].+cod[\w].+', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        attrs = []

        price_usd = response.css('div.itemPrice span.value::text').get().replace(',', '')
        price = {
            'usd': float(price_usd)
        }
        code = response.css('div.item-mfc span.item-mfc-value::text').get().strip('Product ID: ')

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
