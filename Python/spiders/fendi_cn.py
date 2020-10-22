"""
    Author : HuZhibin
    芬迪
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import json
import requests

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'fendi_cn'
    brand_name = 'fendi_cn'
    allowed_domains = ['fendi.cn']
    sitemap_urls = ['https://www.fendi.cn/sitemap.xml']
    sitemap_rules = [
        (r'/url[\w]+.html', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        attrs = []
        json_str = response.css('script::text').get().strip().strip('window.D1M =  ').strip(';')
        json_data = json.loads(json_str)

        code = json_data['params']['sku']
        json_data = requests.get('https://www.fendi.cn/rest/default/V1/applet/product/' + code, headers={
            'Accept': 'application/json, text/plain, */*',
        }).json()

        price_cny = json_data['data']['price'].strip('￥ ').replace(',', '')

        price = {
            'cny': price_cny,
        }

        category = json_data['data']['tracking_category']

        name_part1 = json_data['data']['name']
        name_part2 = json_data['data']['shortDesc']
        name = name_part1 + ' ' + name_part2

        composition = json_data['data']['specificMorer']['composition']
        if composition is not None:
            attrs.append({
                'name': '材质',
                'value': composition,
            })

        depth = json_data['data']['specificMorer']['depth']
        if len(depth):
            attrs.append({
                'name': '深度',
                'value': depth,
            })

        height = json_data['data']['specificMorer']['height']
        if len(height):
            attrs.append({
                'name': '高度',
                'value': height,
            })

        length = json_data['data']['specificMorer']['length']
        if len(length):
            attrs.append({
                'name': '长度',
                'value': length,
            })

        attrs_in_json = json_data['data']['attributes']
        for attr in attrs_in_json:
            n = attr['label']
            v = ','.join([item['label'] for item in attr['values']])
            attrs.append({
                'name': n,
                'value': v,
            })

        description = json_data['data']['description']

        image_urls = [img['big_url'] for img in json_data['data']['images']]

        sku = SKU(self.brand_name, '', category, code, name, response.url, price, description, image_urls, attrs)

        yield sku
