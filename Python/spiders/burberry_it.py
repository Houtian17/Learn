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
    name = 'burberry_it'
    brand_name = 'burberry_it'
    allowed_domains = ['burberry.com']
    sitemap_urls = ['https://it.burberry.com/sitemap-it.xml']
    sitemap_rules = [
        (r'/[-\w]+-p[\d]+', 'parse_sku'),
    ]

    base_url = 'https://it.burberry.com'

    def parse_sku(self, response: Response):
        other_color_urls = [self.base_url + item.attrib['href'] for item in
                            response.css('div.color-picker__swatches a')]
        for url in other_color_urls:
            yield Request(url, callback=self.parse_sku)

        price_eur = response.css('div.product-info-panel__price::text').get()

        if price_eur is None:
            price_eur = response.css('span[data-monogrammedtotal]').attrib['data-monogrammedtotal']
        else:
            price_eur = price_eur.strip('€ ').replace('.', '').replace(',', '.')

        price = {}
        if price_eur is not None:
            price = {
                'eur': float(price_eur),
            }

        json_in_page = response.css('script[type="application/ld+json"]::text').getall()[-1]
        json_data = json.loads(json_in_page)

        code = json_data.get('sku')
        if code is None:
            json_in_page = response.css('#newProductData::text').get()
            json_data = json.loads(json_in_page)
            code = json_data['productID']

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
