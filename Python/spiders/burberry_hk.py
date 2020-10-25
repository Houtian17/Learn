"""
    Author : HuZhibin
    博柏利
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import json

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'burberry_hk'
    brand_name = 'burberry_hk'
    allowed_domains = ['burberry.com']
    sitemap_urls = ['https://hk.burberry.com/sitemap-hk.xml']
    sitemap_rules = [
        (r'/[-\w]+-p[\d]+', 'parse_sku'),
    ]

    base_url = 'https://hk.burberry.com'

    def parse_sku(self, response: Response):
        other_color_urls = [self.base_url + item.attrib['href'] for item in
                            response.css('div.color-picker__swatches a')]
        for url in other_color_urls:
            yield Request(url, callback=self.parse_sku)

        price_hkd = response.css('div.product-info-panel__price::text').get().strip('HKD').replace(',', '')
        price = {
            'hkd': float(price_hkd),
        }

        json_in_page = response.css('script[type="application/ld+json"]::text').getall()[-1]
        json_data = json.loads(json_in_page)

        code = json_data['sku']

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
