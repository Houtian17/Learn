"""
    Author : HuZhibin
    杰尼亚
"""

from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'zagna_cn'
    brand_name = '杰尼亚'
    allowed_domains = ['zegna.cn', 'zegna.com']
    sitemap_urls = ['https://www.zegna.cn/cn-zh/sitemap.xml']
    sitemap_rules = [
        (r'[\w].+product.[\w].+', 'parse_sku')
    ]

    base_url = 'https://www.zegna.cn'

    def parse_sku(self, response: Response):
        attrs = []

        name = response.css('h1.pdpData__name::text').get()
        code = response.css('span.infoProduct__button::text').get()
        description_lines = ['<p>' + item.strip() + '</p>' for item in
                             response.css('div.infoProduct__left p::text').getall() if
                             len(item.strip())]

        desc = ''.join(description_lines)

        price_cny = response.css('span.pdpData__price::text').get().strip().strip('¥ ').replace(',', '')
        price = {
            'cny': float(price_cny)
        }

        image_elements = response.css('img.pdpHeader__zoomImg')
        image_urls = [item.attrib['data-src'].split(',')[-1].strip() for item in image_elements]
        image_urls = [self.base_url + url for url in image_urls]

        sizes = [size.strip() for size in response.css('div.pdpHeader__sizes ul.select__list > li::text').getall()]

        if len(sizes):
            attrs.append({
                'name': '尺码',
                'value': ','.join(sizes)
            })

        color = response.css('div.pdpHeader__color p.pdpColor__value::text').get()
        if color is not None:
            attrs.append({
                'name': '颜色',
                'value': color
            })

        compositions_one = [item.strip() for item in response.css('div.infoProduct__right p::text').getall() if
                            len(item.strip())]
        for s in compositions_one:
            s = s.strip().replace('\n', '')
            attrs.append({
                'name': '参数',
                'value': s
            })

        compositions_two = response.css('h3.infoProduct__subTitle strong::text').get()
        attrs.append({
            'name': '参数',
            'value': compositions_two
        })

        compositions_three = response.css('div.infoProduct__fit span::text').get()
        attrs.append({
            'name': '参数',
            'value': compositions_three
        })

        sku = SKU(self.brand_name, '', '', code, name, response.url, price, desc, image_urls, attrs)
        yield sku
