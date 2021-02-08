import requests
import json

result = requests.get("https://pokeapi.co/api/v2/berry/cheri/")

##https://pokeapi.co/api/v2/charizard/
#print(result.text)
pokemon = result.json()

items = pokemon["item"]
#print(pokemon.keys())

encoded = json.dumps(items)
decoded = json.loads(encoded)

print(decoded['name'])#nombre

link=str((decoded['url']))
atributos=requests.get(link)
caracteristicas=atributos.json()
#rint(caracteristicas.keys())
encoded=json.dumps(caracteristicas)
decoded=json.loads(encoded)
#
print(decoded['attributes'][0]['name'])#atribute

print(decoded['category']['name'])#tiatributo
print(decoded['sprites']['default'])#imagen