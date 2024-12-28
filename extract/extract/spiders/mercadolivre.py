import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br/special-dog-premium-co-adulto-todos-os-tamanhos-carne-15-kg-sacola-seca-1/p/MLB10481547?product_trigger_id=MLB18997398&quantity=1"]

    def parse(self, response):
        
        yield {'ad_name' : response.css('h1.ui-pdp-title::text').get(),
               'price' : response.css('span.andes-money-amount__fraction::text').get(),
               'cents' : response.css('span.andes-money-amount__cents.andes-money-amount__cents--superscript-36::text').get(),       
        }
