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
    name = 'burberry_us'
    brand_name = 'burberry_us'
    allowed_domains = ['burberry.com']
    sitemap_urls = ['https://us.burberry.com/sitemap-us.xml']
    sitemap_rules = [
        (r'/[-\w]+-p[\d]+', 'parse_sku'),
    ]

    base_url = 'https://us.burberry.com'

    def parse_sku(self, response: Response):
        other_color_urls = [self.base_url + item.attrib['href'] for item in
                            response.css('div.color-picker__swatches a')]
        for url in other_color_urls:
            yield Request(url, callback=self.parse_sku)

        price_usd = response.css('div.product-info-panel__price::text').get().strip('$').replace(',', '')
        price = {
            'usd': float(price_usd),
        }

        json_in_page = response.css('script[type="application/ld+json"]::text').getall()[-1]
        json_data = json.loads(json_in_page)

        code = json_data['sku']

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
