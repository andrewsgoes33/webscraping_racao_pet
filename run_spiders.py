from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from extract.spiders.casadoprodutor import CasadoprodutorSpider
from extract.spiders.mercadolivre import MercadolivreSpider
from extract.spiders.magalu import MagaluSpider
from extract.spiders.reidosanimais import ReidosanimaisSpider
from extract.spiders.polipet import PolipetSpider

def run_spiders():
    # Obtém as configurações do projeto
    settings = get_project_settings()
    
    # Cria uma instância do CrawlerProcess com as configurações
    process = CrawlerProcess(settings)
    
    # Adiciona cada spider ao processo
    process.crawl(CasadoprodutorSpider)
    process.crawl(MercadolivreSpider)
    process.crawl(MagaluSpider)
    process.crawl(ReidosanimaisSpider)
    process.crawl(PolipetSpider)
    
    # Inicia o processo de crawling
    process.start()

if __name__ == '__main__':
    run_spiders() 