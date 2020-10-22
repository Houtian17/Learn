"""
    Author : HuZhibin
    麦丝玛拉
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'maxmara_cn'
    brand_name = 'maxmara_cn'
    allowed_domains = ['cn.maxmara.com']
    sitemap_urls = ['https://cn.maxmara.com/sitemap_products.xml?page=0',
                    'https://cn.maxmara.com/sitemap_products.xml?page=1',
                    'https://cn.maxmara.com/sitemap_products.xml?page=2',
                    'https://cn.maxmara.com/sitemap_products.xml?page=3']
    sitemap_rules = [
        (r'/p-[\w-]+$', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        name = response.css('div.details h1::text').get()
        attrs = []

        description = '\n'.join(response.css('#description-tab p::text').getall())
        attrs.append({
            'name': 'Details',
            'value': description,
        })

        composition = '\n'.join(response.css('#composition-tab p::text').getall())
        attrs.append({
            'name': 'Composition and care',
            'value': composition,
        })

        extra_attributes = response.css('div.h5 span::text').getall()

        if extra_attributes is not None and len(extra_attributes) > 1:
            n = extra_attributes[0].strip(':')
            v = extra_attributes[1].strip()
            attrs.append({
                'name': n,
                'value': v,
            })

        code = response.css('div.item p::text').get().strip()

        image_urls = [item.attrib['href'] for item in response.css('ul.thumbnails a')]

        sku = SKU(self.brand_name, '', '', code, name, response.url, {}, description, image_urls, attrs)

        yield sku
