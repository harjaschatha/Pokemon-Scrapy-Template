# -*- coding: utf-8 -*-
import scrapy
import csv
import time

from ..items import Pokemon

HEADER = ('Image URL', "Name",
    # 'Dex Number', 
 # "Type", "Species", "Height", "Weight", "Ability1", "Ability2", "Hidden Ability"
 #            , "Catch Rate", "HP", "Attack", "Defense", "Special Attack", "Special Defense", "Speed"
          )

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
        # item = Pokemon()
        # pokemons = response.css('.infocard-tall-list .infocard-tall')
        # for pokemon in pokemons:
        #
        #     dex_number = pokemon.css('small::text').extract_first()
        #     name = pokemon.css('.ent-name::text').extract_first()
        #     # print(dex_number + " " + name + '\n')
        #     types = pokemon.css('.aside .itype::text').extract()
        #     # print(types)
        #
        #     item['dex_number'] = dex_number
        #     item['name'] = name
        #     item['types'] = types
        #     yield item

        # STEP 1
        # get the names of the pokemon and store in a list
        names = []
        dex = []
        pokemons = response.css('.infocard .text-muted')
        for pokemon in pokemons:
            name = pokemon.css('a.ent-name::text').extract_first()


            names.append(name)
        ### at this point, we will have a list of all pokemons names, called names

        # STEP 2
        
        # we will create a new URL for each pokemon in the pokemons list
        i = 1
        base_url = "https://bulbapedia.bulbagarden.net/wiki/File:"
        for name in names:
            if name == "Farfetch'd":
                name = 'Farfetch\'d'
            elif name == 'Mr. Mime':
                name = "Mr._Mime"
            elif name == 'Nidoran♂':
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
            elif name == 'Giratina':
                name = 'Giratina-Altered'
            elif name == 'Hakamo-O':
                name = 'Hakamo-o'
            elif name == 'Kommo-O':
                name = 'Kommo-o'
            elif name == 'Jangmo-O':
                name = 'Jangmo-o'
            elif name == 'Wishiwashi':
                name = 'Wishiwashi-Solo'
            elif name == 'Oricorio':
                name = 'Oricorio-Baile'
            elif name == 'Sawsbuck':
                name = 'Sawsbuck-Spring'
            elif name == 'Deerling':
                name = 'Deerling-Spring'
            elif name == 'Shaymin':
                name = 'Shaymin-Land'    











            if len(str(i)) == 1:
                url = base_url + '00'+str(i) + name.replace(' ', '-').title() + '.png'
                yield scrapy.Request(url, self.parse_pokemon)
            elif len(str(i)) == 2:
                url = base_url + '0' + str(i) + name.replace(' ', '-').title() + '.png'
                yield scrapy.Request(url, self.parse_pokemon)
            elif len(str(i)) == 3:
                url = base_url + str(i) + name.replace(' ', '-').title() +'.png'
                yield scrapy.Request(url, self.parse_pokemon)

            i = i+1
            print(name)

    def parse_pokemon(self, response):
        # STEP 3
        item = Pokemon()

        #Dex Number
        # dexpath = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[1]/td/strong/text()'
        # dex_number = response.xpath(dexpath).extract_first()
        # item['dex_number'] = dex_number

        # Name = ...
        namepath = '//*[@id="firstHeading"]/text()'
        name = response.xpath(namepath).extract_first()
        item['name'] = name[5:8] + ', ' + name[8:]

        # # Pokemon types
        # typepath1 = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[2]/td/a[1]/text()'
        # type1 = response.xpath(typepath1).extract_first()
        # typepath2 = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[2]/td/a[2]/text()'
        # type2 = response.xpath(typepath2).extract_first()
        # if type(type2) == str:
        #     poketype = type1 + "/" + type2
        # else:
        #     poketype = type1

        # item['types'] = poketype
        # # Pokemon species
        # speciespath = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[3]/td/text()'
        # specie = response.xpath(speciespath).extract_first()
        # item['species'] = specie

        # # Pokemon height
        # heightpath = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[4]/td/text()'
        # height = response.xpath(heightpath).extract_first()
        # item['height'] = height


        # # Pokemon weight
        # weightpath = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[5]/td/text()'
        # weight = response.xpath(weightpath).extract_first()
        # item['weight'] = weight


        # # Abilities
        # abilitynamepath = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[6]/td/a/text()'
        # abilitydescpath = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[6]/td/a/@title'
        # abname = response.xpath(abilitynamepath).extract()
        # abdescript = response.xpath(abilitydescpath).extract()

        # item['ability1'] = abname[0] + ": " + abdescript[0]
        # try:
        #     a = abname[1]
        #     item['ability2'] = abname[1] + ": " + abdescript[1]
        # except IndexError:
        #     item['ability2'] = "-"

        # # Hidden Ability
        # hidden_ability_path_name = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[6]/td/small/a/text()'
        # hidden_ability_path_desc = '/html/body/article/div[3]/ul[2]/li/div[1]/div[2]/table/tbody/tr[6]/td/small/a/@title'
        # hidden_ability_name = response.xpath(hidden_ability_path_name).extract_first()
        # hidden_ability_desc = response.xpath(hidden_ability_path_desc).extract_first()

        # try:
        #     a = hidden_ability_name
        #     item['ability_hidden'] = hidden_ability_name + ": " + hidden_ability_desc
        # except TypeError:
        #     item['ability_hidden'] = "-"
        # # Catch catch

        # catch_rate_path = '/html/body/article/div[3]/ul[2]/li/div[1]/div[3]/div/div[1]/table/tbody/tr[2]/td/text()'
        # catch_rate = response.xpath(catch_rate_path).extract_first()
        # catch_rate = catch_rate.replace(" ", "")
        # item['catch_rate'] = catch_rate


        # # stats
        #     # HP
        # hp_path = '/html/body/article/div[3]/ul[2]/li/div[2]/div[1]/table/tbody/tr[1]/td[1]/text()'
        # hp = response.xpath(hp_path).extract_first()
        # item['hp'] = hp
        #     # attack
        # attack_path = '/html/body/article/div[3]/ul[2]/li/div[2]/div[1]/table/tbody/tr[2]/td[1]/text()'
        # attack = response.xpath(attack_path).extract_first()
        # item['attack'] = attack
        #     # defense
        # defense_path = '/html/body/article/div[3]/ul[2]/li/div[2]/div[1]/table/tbody/tr[3]/td[1]/text()'
        # defense = response.xpath(defense_path).extract_first()
        # item['defense'] = defense
        #     # Sp atk
        # sp_atk_path = '/html/body/article/div[3]/ul[2]/li/div[2]/div[1]/table/tbody/tr[4]/td[1]/text()'
        # sp_atk = response.xpath(sp_atk_path).extract_first()
        # item['sp_atk'] = sp_atk
        #     # Sp Def
        # sp_def_path = '/html/body/article/div[3]/ul[2]/li/div[2]/div[1]/table/tbody/tr[5]/td[1]/text()'
        # sp_def = response.xpath(sp_def_path).extract_first()
        # item['sp_def'] = sp_def
        #     # Speed
        # speed_path = '/html/body/article/div[3]/ul[2]/li/div[2]/div[1]/table/tbody/tr[6]/td[1]/text()'
        # speed = response.xpath(speed_path).extract_first()
        # item['speed'] = speed

        # Image url
        img_path = '//*[@id="file"]/a/img/@src'
        img = response.xpath(img_path).extract_first()
        item['img'] = img


        # # Moveset - Probably different spider



        row = [
            item['name'],
            item['img'],
        #     item['dex_number'],
        #     item['types'],
        #     item['species'],
        #     item['height'],
        #     item['weight'],
        #     item['ability1'],
        #     item['ability2'],
        #     item['ability_hidden'],
        #     item['catch_rate'],
        #     item['hp'],
        #     item['attack'],
        #     item['defense'],
        #     item['sp_atk'],
        #     item['sp_def'],
        #     item['speed']
        ]
        writer.writerow(row)
        # print(item['dex_number'])
        # time.sleep(2)