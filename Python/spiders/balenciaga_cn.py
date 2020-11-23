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
    name = 'balenciaga_cn'
    brand_name = 'balenciaga_cn'
    allowed_domains = ['balenciaga.com',
                       'balenciaga.cn']
    sitemap_urls = ['https://www.balenciaga.com.cn/sitemap.xml']
    sitemap_rules = [
        (r'/products/', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        attrs = []

        name = response.css('p.product-details-section-name__description::text').get().strip()

        price_cny = response.css('div.product-details-section-price__sell-price::text').get().strip().strip('¥ ').replace(',', '')

        price = {
            'cny': float(price_cny)
        }

        color = response.css('span.product-details-section-color__checked-attribute-value::text').get()
        attrs.append({
            'name': '颜色',
            'value': color,
        })

        composition = response.css('div.product-details-section-description__text::text').getall()
        for s in composition:
            attrs.append({
                'name': '参数',
                'value': s
            })

        code = response.url.split('/')[-1].strip('.html').upper()

        page_data = response.xpath('/html/body/script[2]//text()').get()

        image_urls = [item for item in re.findall(r'"(.+?)"', page_data) if 'Large' in item]
        image_urls = utils.list_unique(image_urls)
        image_urls = [url.encode('utf-8').decode('unicode_escape') for url in image_urls]

        sizes = response.css('div.component-size-option::text').getall()
        sizes = [size.strip() for size in sizes]
        if len(sizes):
            attrs.append({
                'name': '尺寸',
                'value': ', '.join(sizes)
            })

        sku = SKU(self.brand_name, '', '', code, name, response.url, price, '', image_urls, attrs)
        yield sku
