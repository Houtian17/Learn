"""
    Author : HuZhibin
    宝格丽
"""
import json
import warnings

import scrapy
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider, Spider
from scrapy.utils.deprecate import method_is_overridden

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'bulgari_cn'
    brand_name = '宝格丽'
    allowed_domains = ['bulgari.cn', 'bulgari.com']
    sitemap_urls = ['https://www.bulgari.cn/sitemap_index.xml']
    sitemap_rules = [
        (r'/zh-cn/', 'parse_sku'),
    ]

    custom_settings = {
        'COOKIES_ENABLED': True,
        'DUPEFILTER_DEBUG': True,
    }

    def start_requests(self):
        for url in self.sitemap_urls:
            yield Request(url, self._parse_sitemap, dont_filter=True)

    def parse_sku(self, response: Response):
        attrs = []
        name_elements = response.css('div.bul-showcase-push-name span::text').get()
        name = name_elements + " " + response.css('div.product-name h1::text').get()
        code = response.css('div[itemprop="sku"]::text').get().strip()
        price = {}
        price_cny = response.css('span.price::text').get()
        if price_cny:
            price_cny = price_cny.strip('¥').replace(',', '').strip()
            price = {
                'cny': float(price_cny),
            }

        sizes = response.css('div.bul-size-select-list ul li::text').getall()
        sizes = [size.strip().strip('尺寸:') for size in sizes]
        if len(sizes):
            attrs.append({
                'name': '尺寸',
                'value': ', '.join(sizes)
            })

        description = response.css('div.bul-edito-texts div.data p::text').get().strip()
        if description is None or len(description) < 1:
            description = response.css('div[itemprop="description"]::text').get()
        # image_elements = response.css('div.fotorama__stage__frame img')
        # image_urls = [item.attrib['src'] for item in image_elements]
        page_data_str = response.css('div.product.media > script[type="text/x-magento-init"]::text').get()
        page_data = json.loads(page_data_str)
        image_data = page_data['[data-gallery-role=gallery-placeholder]']['mage/gallery/gallery']['data']
        image_urls = [img['full'] for img in image_data]
        sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls, attrs)
        yield sku
