import requests
import json

result = requests.get("https://restcountries.eu/rest/v2/all")

#print(result)
#print(result.text)
pais = result.json()

items = pais


encoded = json.dumps(items)
decoded = json.loads(encoded)

print(decoded[0]["name"])
paises=str(decoded[0]["capital"])
print(paises)
paises.replace("[","")
paises.replace("]","")
region=str(decoded[0]["region"])
print(region)
population=str(decoded[0]["population"])
print(population)
cordenadas=str(decoded[0]["latlng"])
print(cordenadas)
idioma=str(decoded[0]["languages"][2])
print(idioma)
imagen=str(decoded[0]["flag"])
print(imagen)


