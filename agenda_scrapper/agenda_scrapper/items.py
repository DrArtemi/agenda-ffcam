# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Excursion(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    activity = scrapy.Field()
    date = scrapy.Field()
    location = scrapy.Field()
    # difficulty_physical = scrapy.Field()
    # difficulty_technical = scrapy.Field()
    accompanist = scrapy.Field()
    inscription_link = scrapy.Field()
    inscription_open = scrapy.Field()