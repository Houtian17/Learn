from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.spiders import CrawlSpider, Rule

from ..items import SKU


class CrawlTemplateSpider(CrawlSpider):
    name = 'longchamp_hk'
    brand_name = 'longchamp_hk'
    allowed_domains = ['longchamp.com']

    # 从哪个 URL 开始
    start_urls = [
        'https://www.longchamp.com/on/demandware.store/Sites-Longchamp-ASIA-Site/zh_HK/Search-UpdateGrid?prefv1=CN&start={}&sz=100'.format(
            start)
        for
        start in range(0, 1400, 100)]

    # 链接提取的规则
    rules = (
        # 回调函数 不会空 时，则调用回调函数Ø
        Rule(LinkExtractor(allow=r'/hk/zh/products/'), callback='parse_sku'),
    )

    def parse_sku(self, response: Response):
        price_hkd = response.css('span.sales::text').get().strip().strip('HK$').replace(',', '')
        price = {
            'hkd': float(price_hkd)
        }

        composition = response.css('ul.list.fs-s.ff-light li::text').getall()
        code = composition[0].strip().strip('參考編號').strip().strip(':').strip()

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
