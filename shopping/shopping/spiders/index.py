import scrapy


class Shoppingspider(scrapy.Spider):
    name='shopping'
    start_urls=['https://www.carbon38.com/shop-all-activewear/tops']

    def parse(self, response):
        for product in response.xpath('//ul[@id="isp_search_results_container"]//li'):
                try:
                       
                    yield{
                        'product_title' : product.css('div.isp_product_title::text').get(),
                        'vendor':product.css('div.isp_product_vendor::text').get(),
                          'sku':product.css('div.isp_product_sku_title::text').get(),
                          'price':product.css('span.isp_product_price::text').get(),
                          'image_link':product.css('a.isp_product_image_href').attrib['href']                       

                         }
                except:
                     yield{
                          'product_title' : product.css('div.isp_product_title::text').get(),
                        'vendor':product.css('div.isp_product_vendor::text').get(),
                          'sku':product.css('div.isp_product_sku_title::text').get(),
                          'price':'sold out',
                          'image_link':product.css('a.isp_product_image_href').attrib['href']                       

                         }

      