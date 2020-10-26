from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from copy import deepcopy

from ..items import SKU


class CrawlTemplateSpider(CrawlSpider):
    name = 'furla_cn'
    brand_name = 'furla_cn'
    allowed_domains = ['furla.cn', 'furla.com']

    # 从哪个 URL 开始
    start_urls = []
    start_urls += [
        'https://www.furla.cn/cn/zh/eshop/%E5%A5%B3%E5%A3%AB/?start={}&sz=50&format=page-element&='.format(start) for
        start in range(0, 375, 50)]
    start_urls += ['https://www.furla.cn/cn/zh/eshop/%E7%94%B7%E5%A3%AB/?start=0&sz=50&format=page-element&=']

    # 链接提取的规则
    rules = (
        # 回调函数 不会空 时，则调用回调函数
        Rule(LinkExtractor(allow=r'furla-.+\.html$'), callback='parse_sku'),
    )

    def parse_sku(self, response: Response):
        attrs = []
        subtitle = response.css('div.sticky h1::text').get() or ''
        title = response.css('div#product-content h2::text').get() or ''
        name = subtitle + title
        all_codes = response.css('div[data-sku]').attrib['data-sku']

        code = response.css('div.product-number div::text').get()
        price_cny = response.css('span.price-sales::text').get()
        if price_cny is not None and len(price_cny) > 1:
            price_cny = price_cny.strip('¥').replace(',', '')
            price = {
                'cny': float(price_cny),
            }

        attribute_names_in_page = response.css('div.row.product-variation div.content-asset::text').getall()
        attribute_values_in_page = response.css(
            'div.row.product-variation div.product-variation__dimension::text').getall()

        for i in range(len(attribute_names_in_page)):
            n = attribute_names_in_page[i].strip()
            v = attribute_values_in_page[i].strip()
            attrs.append({
                'name': n,
                'value': v,
            })

        other_link_elements = response.css('div.swatches.color a.swatchanchor')
        other_variant_urls = [item.attrib['href'] for item in other_link_elements]
        for url in other_variant_urls:
            yield Request(url, callback=self.parse_sku)

        description = response.css('p.product-description::text').get()
        attrs.append({
            'name': '说明',
            'value': description,
        })

        image_elements = response.css('div.small-12.columns.cell-slider-preview  img')
        image_urls = [item.attrib['src'] for item in image_elements]

        details = response.css('div.details div.large-12.columns > div')
        detail_names = [item.css('strong::text').get() for item in details[::2]]
        detail_values = details[1::2].getall()

        for i in range(len(detail_names)):
            n = detail_names[i]
            v = detail_values[i]
            attrs.append({
                'name': n,
                'value': v,
            })

        if all_codes is None or len(all_codes) < 1:
            sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls, attrs)
            yield sku
        else:
            sizes = response.css('.select2-results__options li[id]')
            for i in range(len(all_codes)):
                code = all_codes[i]
                current_attrs = deepcopy(attrs)
                if sizes is not None:
                    size = sizes[i]
                    current_attrs.append({
                        'name': '尺码',
                        'value': size
                    })

                sku = SKU(self.brand_name, '', '', code, name, response.url, price, description, image_urls,
                          current_attrs)
                yield sku
