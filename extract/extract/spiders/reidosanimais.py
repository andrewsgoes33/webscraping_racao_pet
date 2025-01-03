import scrapy
from datetime import datetime


class ReidosanimaisSpider(scrapy.Spider):
    name = "reidosanimais"
    allowed_domains = ["www.reidosanimais.com.br"]
    start_urls = ["https://www.reidosanimais.com.br/racao-seca-special-dog-carne-para-caes-adultos-15kg"]

    def parse(self, response):
        
        yield {'marketplace': 'reidosanimais',
               'ad_name' : response.css('div.prod__name h1::text').get(),
               'price' : response.css('span.price span::text').get().strip(),
               'data_extraction' : datetime.now()
        }
