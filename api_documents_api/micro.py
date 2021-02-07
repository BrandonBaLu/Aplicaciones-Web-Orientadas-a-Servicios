import requests
import json

result = requests.get("https://docs.googleapis.com/$discovery/rest?version=v1")

document = result.json()


servicePath = document["servicePath"]

print(document.keys())
