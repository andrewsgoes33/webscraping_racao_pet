import scrapy


class PolipetSpider(scrapy.Spider):
    name = "polipet"
    allowed_domains = ["www.polipet.com.br"]
    start_urls = ["https://www.polipet.com.br/produto/racao-special-dog-para-caes-adultos-carne-15-kg-92344"]

    def parse(self, response):
       
        yield {'ad_name' : response.css('strong.product__title::text').get(),
               'price' : response.css('div.product__price h2::text').get().strip()
        }

