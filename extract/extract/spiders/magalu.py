import scrapy
from datetime import datetime


class MagaluSpider(scrapy.Spider):
    name = "magalu"
    allowed_domains = ["www.magazineluiza.com.br"]
    start_urls = ["https://www.magazineluiza.com.br/racao-special-dog-premium-carne-para-caes-adultos-15kg-special-dog/p/ddae5kb17j/pe/prac/"]

    def parse(self, response):
        
        yield {'marketplace' : 'magalu',
               'ad_name' : response.css('h1.sc-dcJsrY.jjGTqv::text').get(),
               'price' : response.css('p.sc-dcJsrY.eLxcFM.sc-fmzyuX.dIyuod::text').get().strip(),
               'data_extraction' : datetime.now()
               
        }
