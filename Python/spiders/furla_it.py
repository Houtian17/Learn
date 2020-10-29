from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'furla_it'
    brand_name = 'furla_it'
    allowed_domains = ['furla.com']
    # 从哪个 URL 开始
    sitemap_urls = ['https://www.furla.com/it/en/sitemap.xml']
    sitemap_rules = [
        (r'furla-.+\.html$', 'parse_sku')
    ]

    def parse_sku(self, response: Response):
        code = response.css('div.product-number div::text').get()
        price = {}
        price_eur = response.css('span.price-sales::text').get()
        if price_eur is not None and len(price_eur) > 1:
            price_eur = price_eur.strip('€ ').replace(',', '.')
            price = {
                'eur': float(price_eur),
            }

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], {})
        yield sku
