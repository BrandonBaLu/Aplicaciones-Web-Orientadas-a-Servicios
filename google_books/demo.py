import requests

import json

result =requests.get("https://www.googleapis.com/books/v1/volumes?q=harry+potter") 

print(result.status_code)
print(result.headers["Content-Type"])
books= result.json()



print(books.keys())
print(books["totalItems"])

items = books["items"]
#print(items)
print(items[0].keys())


encoded = json.dump