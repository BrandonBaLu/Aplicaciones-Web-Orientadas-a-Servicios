import requests
import json

result = requests.get("https://www.etnassoft.com/api/v1/get/?sinsajo")

noticia = result.json()

items=noticia
#print(items)

encoded = json.dumps(items)
decoded = json.loads(encoded)

id_lib=str(decoded[0]["ID"])
print(id_lib)

titulo=str(decoded[0]["title"])
print(titulo)

url=str(decoded[0]["url_details"])
print(url)