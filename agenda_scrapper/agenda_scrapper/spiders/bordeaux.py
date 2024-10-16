from pathlib import Path

import scrapy

from agenda_scrapper.items import Excursion


class BordeauxSpider(scrapy.Spider):
    name = "bordeaux"

    start_urls = [
        "https://extranet-clubalpin.com/app/out/out.php?s=12&c=3300&h=be75c3fd58",
    ]

    def parse(self, response):
        excursions = response.css("#sortie_liste .sortie")
        for e in excursions:
            inscription_link = e.css("a.packClub::attr(href)").get()
            yield Excursion(
                id = e.css(".intitule .lienDetail::attr(data-sortie-id)").get(),
                title = e.css(".intitule .lienDetail::text").get().strip(),
                activity = e.css("div div:nth-child(1)::text")[2].get().strip(),
                date = e.css(":nth-child(2)::text")[1].get().strip(),
                location = e.css(".lieu::text").get().strip(),
                accompanist = e.css(":nth-child(5)::text")[1].get().strip(),
                inscription_link = inscription_link,
                inscription_open = inscription_link is not None
            )
            break
