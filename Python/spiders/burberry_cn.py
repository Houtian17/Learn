"""
    Author : HuZhibin
    博柏利
"""
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'burberry_cn'
    brand_name = 'burberry_cn'
    allowed_domains = ['burberry.cn', 'burberry.com']
    sitemap_urls = ['https://cn.burberry.com/sitemap-cn.xml']
    sitemap_rules = [
        (r'/[-\w]+-p[\d]+', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        attrs = []
        image_urls = []

        name = response.css('h1.product-purchase_name::text').get()

        price_cny = response.css('span.product-purchase_price::text').get().strip('¥').replace(',', '')
        price = {
            'cny': float(price_cny),
        }

        color = response.css('li[data-type="colour"] span.product-purchase_selected::text').get()
        attrs.append({
            'name': '颜色',
            'value': color,
        })

        # 爬取其他颜色
        other_color_urls = [self.base_url + item.attrib['href'] for item in
                            response.css('li[data-type="colour"] div.product-purchase_options-labels a')]
        for url in other_color_urls:
            yield Request(url, callback=self.parse_sku)

        description = response.css('div.accordion-tab_content p::text').get()

        attrs_in_page = response.css('div.accordion-tab_sub-item li::text').getall()
        for attr in attrs_in_page:
            parts = attr.split('：', 1)
            n = '参数'
            v = parts[0]
            if len(parts) > 1:
                n = parts[0]
                v = parts[1]
            attrs.append({
                'name': n,
                'value': v,
            })

        if response.css('span[data-label="选择尺码"]').get() is not None:
            sizes = response.css('li[data-type="size"] div.product-purchase_options label::text').getall()
            attrs.append({
                'name': '尺码',
                'value': ','.join(sizes)
            })

        image_elements = response.css('div.product-carousel_item noscript picture img')
        image_urls = ['https://' + (item.attrib['src'].strip('//')) for item in image_elements]

        code = response.css('p.accordion-tab_item-number::text').get().strip("商品 ")

        sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls, attrs)

        yield sku
