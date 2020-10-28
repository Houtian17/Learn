"""
    Author : HuZhibin
    积家cn
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'jaeger-lecoultre_cn'
    brand_name = 'jaeger-lecoultre_cn'
    allowed_domains = ['jaeger-lecoultre.cn', 'jaeger-lecoultre.com']
    sitemap_urls = ['https://www.jaeger-lecoultre.com/cn/sc/home-page/sitemap.xml']
    sitemap_rules = [
        (r'/watches/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        attrs = []
        name = response.css('div.pdp-top__name::text').get()

        if name is None:
            return

        code = response.css('span[itemprop="sku"]::text').get()

        price_cny = response.css('span[itemprop="price"]::text').get().strip().replace('￥', '').replace(',', '')

        price = {
            'cny': float(price_cny)
        }

        description = response.css('span[itemprop="description"]::text').get()

        image_elements = response.css('button.pdp-preview__button img')
        image_urls = [item.attrib['src'] for item in image_elements]
        for i in range(len(image_urls)):
            image_urls[i] = 'https://www.jaeger-lecoultre.cn/' + image_urls[i]

        attribute_names = [n.strip(' :') for n in response.css('#sect2 div b::text').getall()]
        attribute_values = [v.replace('\n', '').replace(' ', '').strip() for v in
                            response.css('#sect2 div::text').getall() if len(v.strip())]

        sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls, attrs)

        yield sku
