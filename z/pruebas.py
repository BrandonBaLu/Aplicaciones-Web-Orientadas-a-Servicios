print(result.text)

print(books.keys())
print(result.headers["Content-Type"])



print(books["totalItems"])

print(result.status_code)


print(items)
print(items[0].keys())


encoded = json.dump




print(pockemon)




import json

# a Python object (dict):
x= {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
