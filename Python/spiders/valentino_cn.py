"""
    Author : HuZhibin
    华伦天奴
"""
from scrapy.http import Request, Response, JsonRequest
from scrapy.spiders import SitemapSpider, Spider
import json

from ..items import SKU


class SitemapTemplateSpider(Spider):
    name = 'valentino_cn'
    brand_name = 'valentino_cn'
    allowed_domains = ['valentino.cn', 'valentino.com']
    ql_url = 'https://www.valentino.cn/graphql'

    def start_requests(self):
        size = 50
        max_page = 33
        for page in range(1, max_page + 1):
            req_body = [{
                "operationName": "fetchProductList",
                "variables": {
                    "input": {
                        "size": size,
                        "page": page,
                        "filters": {
                            'keyword': ''
                        },
                        "breadcrumbFlg": "YES"
                    }
                },
                "query": "query fetchProductList($input: ProductFilters) {  valentino {    products(input: $input) {      pageInfo {                totalCount                size                page                hasNextPage      }        edges {             node {                   code        }      }    }  }}"
            }]
            json_body = json.dumps(req_body)
            yield JsonRequest(self.ql_url, method='POST', body=json_body, callback=self.parse_product_list)

    def parse_product_list(self, response: Response):
        json_data = response.text
        data = json.loads(json_data)[0]['data']['valentino']
        products = data['products']
        edges = products['edges']

        codes = [edge['node']['code'] for edge in edges]

        for code in codes:
            req_body = [{
                "operationName": "fetchProductDetail",
                "variables": {
                    "code": code,
                    "breadcrumbFlg": "NO",
                    "platform": "valentino"
                },
                "query": "query fetchProductDetail($code: ID, $breadcrumbFlg: breadcrumbFlg, $platform: Platform) {  shop {    productDetail(code: $code, breadcrumbFlg: $breadcrumbFlg, platform: $platform) {      userErrors {        code        message      }      product {        code        title        description        images {          url        }        styleProducts {          code          title          images {            url          }          salePrice {            amount            currencyCode          }          skus {            code            salePrice {              amount              currencyCode            }            options {              code              frontName              values {                frontName                code                images {                  url                }              }            }          }          options {            code            frontName            values {              code              frontName              images {                url              }            }          }        }        salePrice {          amount          currencyCode        }        skus {          code          salePrice {            amount            currencyCode          }          options {            code            frontName            values {              frontName              code              images {                url              }            }          }        }        options {          code          frontName          values {            code            frontName            images {              url            }          }          code        }      }    }  }}"
            }]
            json_body = json.dumps(req_body)
            yield JsonRequest(self.ql_url, method='POST', body=json_body, callback=self.parse_product)

    def parse_product(self, response: Response):
        json_data = response.text

        data = json.loads(json_data)[0]['data']['shop']['productDetail']
        product = data['product']
        attrs = []
        code = product['code']
        name = product['title'].replace('\n', '').strip('退仓 ').strip('售罄 ').strip('调货 ')
        desc = product['description']
        image_urls = [img['url'] for img in product['images']]
        cny = product['salePrice']['amount']
        price = {
            'cny': cny,
        }
        link = 'https://www.valentino.cn/zh-cn/' + code

        options = product['options']
        for option in options:
            n = option['frontName']
            v = ','.join([value['frontName'] for value in option['values']])
            attrs.append({
                'name': n,
                'value': v,
            })

        sku = SKU(self.brand_name, '', '', code, name, link, price, desc, image_urls, attrs)

        yield sku
