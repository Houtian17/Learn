from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import SitemapSpider

from ..items import SKU


class SitemapTemplateSpider(SitemapSpider):
    name = 'chaumet_cn'
    brand_name = 'chaumet_cn'
    allowed_domains = ['chaumet.com']
    sitemap_urls = ['https://www.chaumet.com/sitemaps/sitemap_cn.xml']
    sitemap_rules = [
        (r'/zh_hans/(\w|\-)+$', 'parse_sku'),
    ]

    def parse_sku(self, response: Response):
        code = response.css('span[itemprop="sku"]::text').get()
        if code is None:
            return

        name = response.css('div.page-title-wrapper h1::text').get()

        description = response.css('div.description-product p::text').get()

        image_elements = response.css('a.cloud-zoom')
        image_urls = [item.attrib['href'] for item in image_elements]

        if len(image_urls) < 1:
            return

        new_image_urls = []
        for image_url in image_urls:
            url = str(image_url).split('?')[0]
            new_image_urls.append(url)



        names = response.css('table.table-informations th::text').getall()
        values = response.css('table.table-informations td::text').getall()

        attrs = []

        for i in range(0, len(names)):
            n = names[i]
            v = values[i]

            attr = {
                'name': n,
                'value': v,
            }

            attrs.append(attr)

        sku = SKU(self.brand_name, '', '', code, name, response.url, {}, description, new_image_urls, attrs)

        yield sku
