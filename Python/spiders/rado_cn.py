from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
import json
from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'rado_cn'
    brand_name = 'rado_cn'
    allowed_domains = ['rado.cn', 'rado.com']
    sitemap_urls = ['https://www.rado.cn/sitemap.xml']
    sitemap_rules = [
        (r'[\w].+R[0-9].+$', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        attrs = []

        code_elements = response.url
        code = code_elements.split('/')[-1]

        name = response.css('div.swp-hero__info h2::text').get().strip()

        description = response.css('div.text p::text').get()

        json_data = json.loads(response.css('script[type="application/ld+json"]::text').get())

        price_cny = json_data['offers']['price']

        price = {
            'cny': float(price_cny)
        }

        compositions_one_name = [item.strip() for item in
                                 response.css('div.swp-hero__specs strong::text').getall() if len(item.strip())]

        compositions_one_value = [item.strip() for item in
                                  response.css('div.swp-hero__specs p::text').getall() if len(item.strip())]

        if len(compositions_one_name) < 1:
            return

        for i in range(0, len(compositions_one_name)):
            attrs.append({
                'name': compositions_one_name[i],
                'value': compositions_one_value[i]
            })

        compositions_two_name = [item.strip() for item in
                                 response.css('div.swp-specifications__specs strong::text').getall() if
                                 len(item.strip())]

        compositions_two_value = [item.strip() for item in
                                  response.css('div.swp-specifications__specs span::text').getall() if
                                  len(item.strip())]

        for i in range(0, len(compositions_two_name)):
            attrs.append({
                'name': compositions_two_name[i],
                'value': compositions_two_value[i]
            })

        image_elements = response.css('li.swp-gallery__item a')
        image_urls = [item.attrib['href'] for item in image_elements]

        sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls, attrs)
        yield sku
