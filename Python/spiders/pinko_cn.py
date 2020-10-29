"""
    Author : HuZhibin
    品高
"""
from typing import List

from scrapy.http import Response, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import SKU, Product
import re


class CrawlTemplateSpider(CrawlSpider):
    name = 'pinko_cn'
    brand_name = '品高'
    allowed_domains = ['pinko.com', 'pinko-italy.cn']

    start_urls = ['https://www.pinko-italy.cn/%E7%9D%80%E8%A3%85-1/?start={}&sz=50&format=page-element'.format(start)
                  for
                  start in range(0, 700, 50)]
    start_urls += ['https://www.pinko-italy.cn/%E9%85%8D%E4%BB%B6-1/?start={}&sz=50&format=page-element'.format(start)
                   for start in range(0, 350, 60)]
    rules = (
        Rule(LinkExtractor(allow=r'\.html$'), callback='parse_sku'),
    )

    def parse_sku(self, response: Response):
        attrs = []

        name = response.css('h1.product-name::text').get()

        code = response.css('span[itemprop="productID"]::text').get()

        image_elements = response.css('div.product-image')
        image_urls = [item.attrib['data-hires'] for item in image_elements if 'data-hires' in item.attrib]

        desc = response.css('p.product-description--content::text').get()

        color_elements = response.css('ul.swatches.color a')
        color_values = [item.attrib['data-trigger'] for item in color_elements]
        color = ', '.join(color_values)
        attrs.append({
            'name': '颜色',
            'value': color,
        })

        size_elements = response.css('ul.swatches.size a')
        size_values = [item.attrib['data-trigger'] for item in size_elements]
        size = ', '.join(size_values)
        attrs.append({
            'name': '尺寸',
            'value': size,
        })

        compositions_str = response.css('ul.composition-list li::text').getall()
        for s in compositions_str:
            parts = s.split(':', 1)
            n = parts[0].strip()
            v = parts[1].strip()
            attrs.append({
                'name': n,
                'value': v,
            })

        compositions_str2 = response.css('ul.wash-list li::text').getall()
        for s in compositions_str2:
            attrs.append({
                'name': '参数',
                'value': s
            })

        compositions_str3 = response.css('ul.accessoryMeasures-list li::text').getall()
        if compositions_str3 is not None:
            for s in compositions_str3:
                parts = re.split(r'[：:]\s*', s, 1)
                n = parts[0].strip()
                v = parts[1].strip()
                attrs.append({
                    'name': n,
                    'value': v
                })
        colors = [item.attrib['alt'] for item in response.css('ul.swatches.color img')]

        sku = SKU(self.brand_name, '', '', code, name, response.url, {}, desc, image_urls, attrs)

        yield sku
