# -*- coding: utf-8 -*-
import scrapy
import csv
import time

from ..items import Pokemon

HEADER = ("Name", 'Image URL')

output = open('images.csv', 'w', encoding = "utf-8")
writer = csv.writer(output)
writer.writerow(HEADER)


class PokenamesSpider(scrapy.Spider):
    name = 'pokenames'
    start_urls = ['https://pokemondb.net/pokedex/national']

    def start_requests(self):
        urls = self.start_urls
        for url in urls:
            yield scrapy.Request(url, self.parse_pokemons)

    def parse_pokemons(self, response):
        names = []
        dex = []
        pokemons = response.css('.infocard .text-muted')
        for pokemon in pokemons:
            name = pokemon.css('a.ent-name::text').extract_first()


            names.append(name)
        ### at this point, we will have a list of all pokemons names, called names
        
        # we will create a new URL for each pokemon in the pokemons list
        # But some names need exceptions as the URLs do not match
        base_url = "https://bulbapedia.bulbagarden.net/wiki/File:"
        for name in names:
            if name == "Farfetch'd":
                name = 'Farfetch\'d'
            elif name == 'Mr. Mime':
                name = "Mr._Mime"
            elif name == 'Nidoran♂': #For male and female, it depends on the sites urls
                name = 'Nidoran'
            elif name == 'Nidoran♀':
                name = 'Nidoran'
            elif name == 'Mime Jr.':
                name = 'Mime_Jr'
            elif name == 'Flabébé':
                name = 'Flabébé'
            elif name == 'Type: Null':
                name = 'Type_Null'
            elif name == 'Tapu Koko':
                name = 'Tapu_Koko'
            elif name == 'Tapu Lele':
                name = 'Tapu_Lele'
            elif name == 'Tapu Bulu':
                name = 'Tapu_Bulu'
            elif name == 'Tapu Fini':
                name = 'Tapu_Fini'
        
            print(name)

    def parse_pokemon(self, response):
        # STEP 3
        item = Pokemon()

        row = [
            item['name'],
            item['img'],
        ]
        writer.writerow(row)