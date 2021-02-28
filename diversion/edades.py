import web
import json
urls = (
    '/personas?', 'Personas'
)
app = web.application(urls, globals())

class Personas():

  json_file={}

  def read(self):
    try:
      with open("datos.json") as file:
        self.json_file = json.load(file)
      print(self.json_file)
      return json.dumps(self.json_file)

    except Exception as error:
      print("Error {}".format(error.args[0]))

  def writePersonas(self, nombre, dia, mes, ano, edad):
    data={
    "Nombre" : nombre,
    "Dia" : dia,
    "Mes" : mes,
    "Ano de nacimiento" : ano,
    "Edad" : edad
    }
   
    with open("datos.json") as file:
        self.json_file = json.load(file)
    self.json_file["personas"].append(data)
    with open("datos.json","w") as file:
      json.dump(self.json_file, file)
    return self.read()


  def GET(self):
    try:
      parametros = web.input() 
      action = parametros["action"]      

      if action == "get":
        return self.read()
        
      elif action == "put":
        nombre = parametros.nombre
        dia = int(parametros.dia)
        mes = parametros.mes
        ano = int(parametros.ano)
        edad = 2021 - ano
        self.writePersonas(nombre, dia, mes, ano, edad)
        mensaje = {}
        mensaje["mensaje"]= "Datos almacenados"
        return json.dumps(mensaje)
    except:
      data = {}
      data["mensaje"] = "Revisa tus datos ingresados"
      return json.dumps(data)
       

if __name__ == "__main__":
  app.run()


