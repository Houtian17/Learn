from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
import re
from scrapy.spiders import CrawlSpider, Rule

from ..items import SKU


class CrawlTemplateSpider(CrawlSpider):
    name = 'longchamp_cn'
    brand_name = '珑骧'
    allowed_domains = ['longchamp.com', 'longchamp.cn']

    # 从哪个 URL 开始
    start_urls = [
        'https://www.longchamp.cn/on/demandware.store/Sites-Longchamp-ASIA-Site/zh_CN/Search-UpdateGrid?prefv1=CN&start={}&sz=100'.format(
            start)
        for
        start in range(0, 1300, 100)]

    # 链接提取的规则
    rules = (
        # 回调函数 不会空 时，则调用回调函数Ø
        Rule(LinkExtractor(allow=r'/cn/zh/products/'), callback='parse_sku'),
    )

    def parse_sku(self, response: Response):
        name_elements = response.css('h1.product-title::text').get().strip()
        name = name_elements + response.css('span.c-gray-epsilon::text').get()

        price_cny = response.css('span.sales::text').get().strip().replace(',', '').strip('¥')
        price = {
            'cny': float(price_cny)
        }

        color = response.css('ul.list.product-color li span.sr-only::text').get()
        description = ''
        description_elements = response.css('p.read-more.pb-3::text').get().strip()
        description_elements2 = response.css('p.read-more span.read-more__content::text').get()
        if description_elements2 is not None:
            description = description_elements + description_elements2.strip()
        else:
            description = description_elements

        image_elements = response.css('div.product_carousel div.product-media__inner source')
        image_urls = [item.attrib['srcset'] for item in image_elements]
        image_urls = [re.sub(r'\?.+', '', url) for url in image_urls]

        composition = response.css('ul.list.fs-s.ff-light li::text').getall()
        code = composition[0].strip().strip('编号').strip().strip(':').strip()

        attrs = []

        for s in composition[1:]:
            parts = s.split(':')
            n = '参数'
            v = s
            if len(parts) > 1:
                n = parts[0]
                v = parts[1]

            attrs.append({
                'name': n,
                'value': v,
            })

        sizes = response.css('#select-size option[data-attr-value]::text').getall()
        attrs.append({
            'name': '颜色',
            'value': color,
        })

        sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls, attrs)

        yield sku
