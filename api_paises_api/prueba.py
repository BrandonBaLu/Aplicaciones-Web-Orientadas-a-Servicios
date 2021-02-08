import requests
import json

result = requests.get("https://restcountries.eu/rest/v2/all")

#print(result)
#print(result.text)
pais = result.json()

items = pais


encoded = json.dumps(items)
decoded = json.loads(encoded)

paises=str(decoded[0]["name"])
print(paises)
capital=str(decoded[0]["capital"])
print(capital)
capital.replace("[","")
capital.replace("]","")
region=str(decoded[0]["region"])
print(region)
population=str(decoded[0]["population"])
print(population)
cordenadas=str(decoded[0]["latlng"])
print(cordenadas)
idioma=str(decoded[0]["languages"][0])
print(idioma)
imagen=str(decoded[0]["flag"])
print(imagen)


