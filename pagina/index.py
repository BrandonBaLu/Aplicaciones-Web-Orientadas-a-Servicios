import web
import requests
import json

render= web.template.render("pagina/")

class Index():
  def GET(self):
    datos=None
    return render.index(datos)

  def POST(self)  :
    form=web.input()
    paises=form.pais
    
    result = requests.get("https://restcountries.eu/rest/v2/name/"+paises)

    pais = result.json()

    items = pais

    encoded = json.dumps(items)
    decoded = json.loads(encoded)

    paises=str(decoded[0]["name"])
    capital_1=str(decoded[0]["capital"])
    region_1=str(decoded[0]["region"])
    population_1=str(decoded[0]["population"])
    cordenadas_1=str(decoded[0]["latlng"])
    idioma_1=str(decoded[0]["languages"][0])
    imagen_1=decoded[0]["flag"]
    
    pais="<label>'"+paises+"'</label>"
    capital="<label>'"+capital_1+"'</label>"
    region="<label>'"+region_1+"'</label>"
    population="<label>'"+population_1+"'</label>"
    cordenadas="<label>'"+cordenadas_1+"'</label>"
    idioma="<label>'"+idioma_1+"'</label>"
    imagen ="<img src='"+imagen_1+"'/>"
    

    datos={
      "países":"Nombre del país: "+pais,
      "capital":"capital: "+capital,
      "region": "Region: "+region,
      "population": "Population: "+population,
      "cordenadas":"Cordenadas: "+cordenadas,
      "idioma": "idioma: "+idioma,
      "imagen":imagen
    }
    return render.index(datos)





