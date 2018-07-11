# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Pokemon(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # name = scrapy.Field()
    dex_number = scrapy.Field()
    types = scrapy.Field()
    species = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    ability1 = scrapy.Field()
    ability2 = scrapy.Field()
    ability_hidden = scrapy.Field()
    catch_rate = scrapy.Field()
    hp = scrapy.Field()
    attack = scrapy.Field()
    defense = scrapy.Field()
    sp_atk = scrapy.Field()
    sp_def = scrapy.Field()
    speed = scrapy.Field()
    img = scrapy.Field()
