import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Ajusta o PYTHONPATH para incluir o diretório correto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from extract.extract.spiders.casadoprodutor import CasadoprodutorSpider
from extract.extract.spiders.mercadolivre import MercadolivreSpider
from extract.extract.spiders.magalu import MagaluSpider
from extract.extract.spiders.reidosanimais import ReidosanimaisSpider
from extract.extract.spiders.polipet import PolipetSpider

def run_spiders():
    # Obtém as configurações do projeto
    settings = get_project_settings()
    
    # Configura o arquivo de saída
    settings.update({
        'FEEDS': {
            'data/data.jsonl': {
                'format': 'jsonlines',
                'encoding': 'utf8'
            }
        }
    })
    
    # Garante que o diretório data existe
    os.makedirs('data', exist_ok=True)
    
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