from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU
import requests
import re
import json


class SitemapTemplateSpider(SitemapSpider):
    name = 'iwc_hk'
    brand_name = '万国'
    allowed_domains = ['iwc.com']
    sitemap_urls = ['https://www.iwc.com/zh-tw.sitemap.xml']
    sitemap_rules = [
        ('/zh-tw/watch-collections/', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code = response.css('h2.iwc-buying-options-reference::text').get()
        if code is None:
            return

        product_full_name = response.css('input#loginpagepath').attrib['value'].rsplit('/')[-1]

        price_url = 'https://www.iwc.com/zh-tw/watch-collections/pilot-watches/{}.productinfo.HK.json'.format(
            product_full_name)

        price_data: dict = requests.get(price_url).json()
        k = list(price_data.keys())[0]
        hkd = price_data[k]['price']

        price = {
            'hkd': float(hkd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
