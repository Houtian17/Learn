"""
    Author : HuZhibin
    麦丝玛拉
"""
import logging

from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider
from scrapy.spiders.sitemap import iterloc
from scrapy.utils.sitemap import sitemap_urls_from_robots, Sitemap

from ..items import SKU

logger = logging.getLogger(__name__)


class SitemapTemplateSpider(SitemapSpider):
    name = 'maxmara_us'
    brand_name = 'maxmara_us'
    allowed_domains = ['maxmara.com']
    sitemap_urls = ['https://us.maxmara.com/sitemap_products.xml?page=0',
                    'https://us.maxmara.com/sitemap_products.xml?page=1',
                    'https://us.maxmara.com/sitemap_products.xml?page=2']
    sitemap_rules = [
        (r'/p-[\w-]+$', 'parse_sku'),
    ]

    custom_settings = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36'
    }

    def parse_sku(self, response: Response):

        price = {}
        usd: str = response.css('span.price::text').get()
        if usd is not None:
            usd = usd.strip('$').replace(',', '').strip()
            price = {
                'usd': usd,
            }

        code = response.css('div.item p::text').get()

        sku = SKU(self.brand_name, '', '', code, '', response.url, price, '', [], [])

        yield sku
