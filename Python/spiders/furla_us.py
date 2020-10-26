from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'furla_us'
    brand_name = 'furla_us'
    allowed_domains = ['furla.com']
    # 从哪个 URL 开始
    sitemap_urls = ['https://www.furla.com/us/en/sitemap.xml']
    sitemap_rules = [
        (r'furla-.+\.html$', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code = response.css('div.product-number div::text').get()

        price_usd = response.css('span.price-sales::text').get()
        if price_usd is not None and len(price_usd) > 1:
            price_usd = price_usd.strip('$').replace(',', '')
            price = {
                'usd': float(price_usd),
            }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', {}, {})
        yield sku
