import scrapy
from war.items import WarItem


class WarspiderSpider(scrapy.Spider):
    name = "warspider"
    allowed_domains = ["fr.wikipedia.org"]
    start_urls = ["https://fr.wikipedia.org/wiki/Guerre_du_Vi%C3%AAt_Nam"]

    def parse(self, response):
        item = WarItem()
        item["name"] = response.xpath("//div[@class='entete icon defaut']/div/text()").extract_first()
        information_generales = response.css(".infobox_v3 > table")
        item["date"] = information_generales.xpath(".//th[contains(text(), 'Date')]/following-sibling::td/time/text()").extract_first()
        item["lieu"] = information_generales.xpath(".//th[contains(text(), 'Lieu')]/following-sibling::td/a/text()").extract_first()# extract_first()  retourne le premier élément de la liste en format texte
        elemnt = information_generales.xpath(".//th[contains(text(), 'Issue')]/following-sibling::td/p")
        item["issue"] = elemnt.xpath(".//text()").extract()
        item["issue"] = " ".join(item["issue"])
        liste_belligerents = information_generales.xpath(".//tr[@class='left vborder']")# liste des belligerents
        item["belligerents"] = liste_belligerents.xpath(".//text()").extract()
        yield item
        guerres_urls = response.xpath("//a[contains(@href, '/wiki/Guerre')]/@href").extract()# recupere sous forme de liste les urls des guerres
        for url in guerres_urls:
            print(url)
            full_url = response.urljoin(url)
            yield response.follow(full_url, callback=self.parse)

