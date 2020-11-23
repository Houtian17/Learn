from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.spiders import CrawlSpider, Rule

from ..items import SKU


class CrawlTemplateSpider(CrawlSpider):
    name = 'longchamp_us'
    brand_name = 'longchamp_us'
    allowed_domains = ['longchamp.com']

    # 从哪个 URL 开始
    start_urls = [
        'https://www.longchamp.com/on/demandware.store/Sites-Longchamp-NA-Site/en_US/Search-UpdateGrid?prefv1=US&start={}&sz=100'.format(
            start)
        for
        start in range(0, 1800, 100)]

    # 链接提取的规则
    rules = (
        # 回调函数 不会空 时，则调用回调函数Ø
        Rule(LinkExtractor(allow=r'/us/en/products/'), callback='parse_sku'),
    )

    def parse_sku(self, response: Response):
        price_usd = response.css('span.sales::text').get().strip().strip('$').replace(',', '')
        price = {
            'usd': float(price_usd)
        }

        composition = response.css('ul.list.fs-s.ff-light li::text').getall()
        code = composition[0].strip().strip('Reference').strip().strip(':').strip()

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
