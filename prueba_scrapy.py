import scrapy
# Esta biblioteca permite hacer webcrolling de manera recursiva
from scrapy.crawler import CrawlerProcess

# scrapy nos pide que trabajemos definiciendo clases
class Spider12(scrapy.Spider):
    name = 'spider12'
    # Para definir que dominio queremos scrapear y cuales no.
    # Se le puede pasar una lista
    allowed_domains = ['pagina12.com.ar'] # Le estamos diciendo que solamente queremos scrapear dominios que esten dentro de pagina12.com.ar
    # Configurar el tipo de archivo de salida
    # DEPTH_LIMIT es el limite para scrapear
    custom_settings = {'FEED_FORMAT':'json',
                      'FEED_URI':'resultados.json',
                      'DEPTH_LIMIT': 2,
                      'FEED_EXPORT_ENCODING': 'utf-8'}
    start_url = ['https://www.pagina12.com.ar/281434-espinoza-lo-que-no-hicieron-en-4-anos-lo-hicimos-en-tres-mes',
 'https://www.pagina12.com.ar/281424-reforma-judicial-juntos-por-el-cambio-no-quiere-que-se-ampli',
 'https://www.pagina12.com.ar/281419-cinco-claves-sobre-el-flamante-registro-de-trabajadores-de-l',
 'https://www.pagina12.com.ar/281341-alberto-fernandez-inauguro-el-hospital-favaloro-en-la-matanz',
 'https://www.pagina12.com.ar/281127-plan-condor-argentina-es-el-pais-que-mas-avanzo-en-el-juzgam',
 'https://www.pagina12.com.ar/281289-se-viene-el-informe-en-diputados',
 'https://www.pagina12.com.ar/281132-causa-peajes-guillermo-dietrich-fue-procesado-por-administra',
 'https://www.pagina12.com.ar/281134-alberto-fernandez-inauguro-el-plenario-de-la-cta-y-convoco-a',
 'https://www.pagina12.com.ar/281139-daniel-gollan-si-se-disparan-los-casos-por-encima-de-un-nume',
 'https://www.pagina12.com.ar/281151-coronavirus-murieron-dos-represores-presos-contagiados',
 'https://www.pagina12.com.ar/281212-reforma-judicial-el-presidente-definio-los-11-nombres-que-in',
 'https://www.pagina12.com.ar/281243-alfredo-cornejo-lo-quiere-a-mauricio-macri-en-cambiemos-pero',
 'https://www.pagina12.com.ar/281266-la-crisis-del-poder-judicial-y-la-necesidad-de-su-reforma']
    
    # Definir un metodo que procese la respuesta de cada solicitud que se haga a cada una de las urls
    def parse(self, response):
        # Articulo promocionado
        nota_promocionada = response.xpath('//div[@class="article-title "]/a/@href').get()
        if nota_promocionada is not None:
            yield response.follow(nota_promocionada, callback=self.parse_nota)
    
        # Listado de notas
        notas = response.xpath('//div[@class="article-footer"]//div[@id="cxense-read-more-widget-283845"]//a/@href').getall()
        for nota in notas:
            yield response.follow(nota, callback=self.parse_nota)
        
        # Link a la sigueinte pagina
        # por si hay algun boton
        # next_page = response.xpath('')
        # if next_page is not None:
            # yield response.follow(next_page, callback=self.parse)
    
    def parse_nota(self, response):
        # Parseo de la nota
        titulo = response.xpath('//div[@class="article-titles"]/h1[@class="article-title"]/text()').get()
        cuerpo = ''.join(response.xpath('//div[@class="article-text"]/p/text()').getall())
        # guaradr la informacion en el json que habiamos definido
        yield {'url': response.url,
                'titulo': titulo,
                'cuerpo': cuerpo}   

if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(Spider12)
    process.start()