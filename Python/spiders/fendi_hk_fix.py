"""
    Author : HuZhibin
    芬迪
"""
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import SKU


class FendiSpider(CrawlSpider):
    name = 'fendi_hk'
    brand_name = 'fendi_hk'
    allowed_domains = ['fendi.com']

    # 从哪个 URL 开始
    start_urls = ['https://www.fendi.com/hk/']

    rules = (
        # 回调函数 不会空 时，则调用回调函数
        Rule(LinkExtractor(allow=r'.+/hk/.+'), follow=True, callback='parse_sku'),
    )

    def parse_sku(self, response: Response):
        code = response.css('span[itemprop="productID"]::text').get()
        if code is None:
            print('当前地址应该不是详情页：', response.url)
            return

        price_hkd = response.css('meta[itemprop="price"]').attrib['content']

        price = {
            'hkd': price_hkd,
        }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
