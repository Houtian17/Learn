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
    name = 'balenciaga_it'
    brand_name = 'balenciaga_it'
    allowed_domains = ['balenciaga.com']
    sitemap_urls = ['https://www.balenciaga.com/sitemap_it_balenciaga.xml']
    sitemap_rules = [
        (r'[\w].+cod[\w].+', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        attrs = []

        price_eur = response.css('div.itemPrice span.value::text').get().replace('.', '').replace(',', '.')
        price = {
            'eur': float(price_eur)
        }

        code = response.css('div.item-mfc span.item-mfc-value::text').get().strip('Modello: ')

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
