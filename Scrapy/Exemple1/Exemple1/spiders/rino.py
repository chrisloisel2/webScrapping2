import scrapy
from Exemple1.items import Rhino

class RinoSpider(scrapy.Spider):
    name = "rino"
    allowed_domains = ["fr.wikipedia.org"]
    start_urls = ["https://fr.wikipedia.org/wiki/Rhinoc%C3%A9ros"]

    def parse(self, response):
        item = Rhino()
        # -> Extraction des données de la page
        # balise = response.css("a").extract()
        # -> une seule balise
        # balise = response.css("a").extract_first()
        # -> une seule balise via xpath
        # balise = response.xpath("//a").extract_first()
        # balise = response.xpath("//*[@class='mw-jump-link']/text()").extract()
        item['nom'] = response.xpath("//*[@class='mw-logo']/@href").extract()
        item['types'] = response.xpath("//*[@title='Mammifère']/text()").extract()
        item['image'] = response.xpath("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[2]/div[2]/span/a/img/@src").extract()
        yield item
