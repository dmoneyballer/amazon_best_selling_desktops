# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    desciption = scrapy.Field()
    rating = scrapy.Field()
    number_of_ratings = scrapy.Field()
    price = scrapy.Field()
    # pass
