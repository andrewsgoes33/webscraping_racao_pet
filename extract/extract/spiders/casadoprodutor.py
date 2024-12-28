import scrapy


class CasadoprodutorSpider(scrapy.Spider):
    name = "casadoprodutor"
    allowed_domains = ["www.casadoprodutor.com.br"]
    start_urls = ["https://www.casadoprodutor.com.br/rac-o-special-dog-carne-c-es-adultos-15kg.html"]

    def parse(self, response):
        yield {
            'ad_name': response.css('span.base::text').get(),
            'price': response.css('span#product-price-10813 span.price::text').get().strip()
        }
