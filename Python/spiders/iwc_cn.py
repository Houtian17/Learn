from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU
import re
import json


class SitemapTemplateSpider(SitemapSpider):
    name = 'iwc_cn'
    brand_name = '万国'
    allowed_domains = ['iwc.cn', 'iwc.com']
    sitemap_urls = ['https://www.iwc.cn/cn/zh-cn.sitemap.xml']
    sitemap_rules = [
        ('/zh-cn/watch-collections/', 'parse_sku')
    ]

    base_url = 'https://www.iwc.cn'

    def parse_sku(self, response: Response):
        attrs = []

        code = response.css('h2.iwc-buying-options-reference::text').get()
        name = response.css('h3.iwc-buying-options-title::text').get().strip()
        description = '<br>'.join(
            response.css('ul[data-toggle-id="showDetails1"] li.iwc-product-detail-item::text').getall())

        tracking_product = json.loads(response.css('button[data-tracking-product]').attrib['data-tracking-product'])
        cny = tracking_product['price']

        price = {
            'cny': float(cny)
        }

        image_elements = response.css('div.rcms_productPageThumbnails')
        image_urls = [item.attrib['data-src'] for item in image_elements]
        image_urls = [self.base_url + url for url in image_urls]
        image_urls = [re.sub(r'\.transform.+', '', url) for url in image_urls]

        compositions_one = [item.strip() for item in response.css('ul[data-toggle-id="showDetails0"] li::text').getall()
                            if len(item.strip())]
        for s in compositions_one:
            s = s.strip().replace('\n', '')
            attrs.append({
                'name': '表壳',
                'value': s
            })

        compositions_three = [item.strip() for item in
                              response.css('ul[data-toggle-id="showDetails2"] li::text').getall() if len(item.strip())]
        for s in compositions_three:
            s = s.strip().replace('\n', '').replace(' ', '')
            attrs.append({
                'name': '机芯',
                'value': s
            })

        compositions_four = [item.strip() for item in
                             response.css('ul[data-toggle-id="showDetails3"] li::text').getall() if len(item.strip())]
        for s in compositions_four:
            s = s.strip().replace('\n', '')
            attrs.append({
                'name': '表带',
                'value': s
            })

        compositions_two = [item.strip() for item in response.css('ul[data-toggle-id="showDetails4"] li::text').getall()
                            if len(item.strip())]
        for s in compositions_two:
            s = s.strip().replace('\n', '')
            attrs.append({
                'name': '表盘',
                'value': s
            })
        sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls, attrs)
        yield sku
