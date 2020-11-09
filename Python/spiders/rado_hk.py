from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import requests
from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'rado_hk'
    brand_name = 'rado_hk'
    allowed_domains = ['rado.com']
    sitemap_urls = ['https://www.rado.com/sitemap.xml']
    sitemap_rules = [
        (r'[\w].+R[0-9].+$', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code_elements = response.url
        code = code_elements.split('/')[-1]

        node_id = response.css('section[data-nodeid]').attrib['data-nodeid']

        price_data = requests.get('https://www.rado.com/api/product-price/' + str(node_id)).json()
        price_hkd = price_data['price'].strip('HKD ').replace('\'', '')
        price = {
            'hkd': float(price_hkd)
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])
        yield sku
