import web
import json
carta = {}
urls = (
    '/(.*)',
    'Carta',
)
app = web.application(urls, globals())

class Carta():
  def GET(self, carta_astral):
    try:
      fech_dia = int(carta_astral[0:2])
      fech_mes = int(carta_astral[3:5])
      print(fech_dia, fech_mes)
      
      
      if fech_dia >= 21 or fech_dia <= 19 and fech_mes == 1 or fech_mes == 2:
        horoscopo = {}
        horoscopo["Nombre"] = "Acuario"
        horoscopo["Fecha"] = "Enero  21 – Febrero 19"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "7, 14 y 20"
        horoscopo["Color"] = "Gris, azul y verde"
        horoscopo["Horóscopo del día"] = "Estarás inexplicablemente tenso, pese a las mil y una bondades que te reserva la jornada. No olvides que todo pasa."
        result = json.dumps(horoscopo)
        return result
         
      elif fech_dia >= 20 or fech_dia <= 20 and fech_mes == 2 or fech_mes == 3:
        horoscopo = {}
        horoscopo["Nombre"] = "Picis"
        horoscopo["Fecha"] = "Febrero  20 – Marzo 20"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "75, 11 y 19"
        horoscopo["Color"] = "Verde, azul y morado."
        horoscopo["Horóscopo del día"] = "Escucha una propuesta que rompe con tus prejuicios. Un elogio llega desde el lugar menos esperado. No lo descartes."
        result = json.dumps(horoscopo)
        return result

      elif fech_dia >= 21 or fech_dia <= 19 and fech_mes == 3 or fech_mes == 4:
        horoscopo = {}
        horoscopo["Nombre"] = "Aries"
        horoscopo["Fecha"] = "Marzo  21 – Abril 19"
        horoscopo["Elemento"] = "Fuego"
        horoscopo["Numero de la suerte"] = " 7, 17 y 21."
        horoscopo["Color"] = "Gris, azul y verde"
        horoscopo["Horóscopo del día"] = "Contarás con una energía potenciada para encarar los cambios que tanto deseas. Te adaptarás a los tiempos que se avecinan."

      elif fech_dia >= 20 or fech_dia <= 20 and fech_mes == 4 or fech_mes == 5:
        horoscopo = {}
        horoscopo["Nombre"] = "Tauro"
        horoscopo["Fecha"] = "Abril  20 – Mayo 20"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = "4, 6 y 11."
        horoscopo["Color"] = "Verde claro, rosa y turquesa."
        horoscopo["Horóscopo del día"] = "Para encontrar la solución, separa cada cosa y analiza cada plano. Sentirás todo el apoyo familiar y de tu entorno más cercano."
        result = json.dumps(horoscopo)
        return result 

      elif fech_dia >= 21 or fech_dia <= 21 and fech_mes == 5 or fech_mes == 6:
        horoscopo = {}
        horoscopo["Nombre"] = "Géminis"
        horoscopo["Fecha"] = "Mayo  21 – Junio 21"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "2, 4, 7 y 9"
        horoscopo["Color"] = "Azul, violeta y amarillo"
        horoscopo["Horóscopo del día"] = "Mientras tú quieres hacer un balance y cerrar una etapa surgirán otras alternativas y nuevos caminos para recorrer."
        result = json.dumps(horoscopo)
				return resul

      elif fech_dia >= 20 or fech_dia <= 20 and fech_mes == 6 or fech_mes == 7:
        horoscopo = {}
        horoscopo["Nombre"] = "Cáncer"
        horoscopo["Fecha"] = "Junio  20 – Julio 20"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "5, 6, 8 y 19."
        horoscopo["Color"] = "Blanco, plateado y verde"
        horoscopo["Horóscopo del día"] = "Hoy tendrás un muy buen día, en el que las buenas noticias podrían llegar cuando menos lo imagines. Debes aprovechar el momento."
        result = json.dumps(horoscopo)
				return resul

      elif fech_dia >= 22 or fech_dia <= 22 and fech_mes == 7 or fech_mes == 8:
        horoscopo = {}
        horoscopo["Nombre"] = "Leo"
        horoscopo["Fecha"] = "Julio  22 – Agosto 22"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "1, 9, 10."
        horoscopo["Color"] = "Dorado, naranja y verde."
        horoscopo["Horóscopo del día"] = "Tu capacidad de entrega a los problemas ajenos aumenta cada día. Tendrás mucha decisión para ayudar. Serás recompensado."
        result = json.dumps(horoscopo)
				return resul

      elif fech_dia >= 23 or fech_dia <= 22 and fech_mes == 8 or fech_mes == 9:
        horoscopo = {}
        horoscopo["Nombre"] = "Virgo"
        horoscopo["Fecha"] = "Agosto  23 – Septiembre 22"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = "10, 15 y 27."
        horoscopo["Color"] = "Blanco, violeta y naranja."
        horoscopo["Horóscopo del día"] = "Será mejor que comiences a planificar mejor tu vida, al menos en los aspectos básicos. No permitas que las cosas simplemente te sucedan."
        result = json.dumps(horoscopo)
				return resul

      elif fech_dia >= 23 or fech_dia <= 2 and fech_mes == 9 or fech_mes == 10:
        horoscopo = {}
        horoscopo["Nombre"] = "Libra"
        horoscopo["Fecha"] = "Septiembre  23 – Octubre 22"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "2, 8, 19"
        horoscopo["Color"] = "Rosa, azul y verde."
        horoscopo["Horóscopo del día"] = "Período para el aprendizaje, el cambio de hábito y buscar nuevas oportunidades. Agenda tus citas de trabajo, evita contratiempos."
        result = json.dumps(horoscopo)
				return resul


      elif fech_dia >= 23 or fech_dia <= 21 and fech_mes == 10 or fech_mes == 11:
        horoscopo = {}
        horoscopo["Nombre"] = "Escorpio"
        horoscopo["Fecha"] = "Octubre  23 – Noviembre 21"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "4, 13 y 21."
        horoscopo["Color"] = "Rojo, verde y negro"
        horoscopo["Horóscopo del día"] = "Golpe de suerte. Buena fortuna en los negocios, el estudio, los viajes y los juegos de azar. Toma la iniciativa y triunfarás."
        result = json.dumps(horoscopo)
				  return resul

      elif fech_dia >= 22 or fech_dia <= 21 and fech_mes == 11 or fech_mes == 12:
        horoscopo = {}
        horoscopo["Nombre"] = "Sagitario"
        horoscopo["Fecha"] = "Noviembre  20 – Diciembre 20"
        horoscopo["Elemento"] = "Fuego"
        horoscopo["Numero de la suerte"] = " 3, 8, 13."
        horoscopo["Color"] = "Blanco, azul y verde."
        horoscopo["Horóscopo del día"] = "Agresiones cruzadas te tendrán a mal traer. Pese a estar libre de las cadenas que te tenían atado habrá problemas sentimentales."
        result = json.dumps(horoscopo)
				return resul
          
      elif fech_dia >= 22 or fech_dia <= 20 and fech_mes == 12 or fech_mes == 1:
        horoscopo = {}
        horoscopo["Nombre"] = "Capricornio"
        horoscopo["Fecha"] = "Diciembre  22 – Enero 20"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = " 3, 6, 16."
        horoscopo["Color"] = "Negro, azul y marrón."
        horoscopo["Horóscopo del día"] = "El fruto de tu esfuerzo y perseverancia te permitirán comprar ropa, calzado, perfumes y accesorios necesarios para verte mejor."
        result = json.dumps(horoscopo)
				return resul
    except:
      horoscopo = {}
			horoscopo["Dato"] = "El dato: " + str(carta_astral)
			horoscopo["Error"] = "Valor incorrecto"
			horoscopo[
			    "Solucion"] = "Ingresa la fecha de tu nacimiento formato DD/MM/AAAA"
			result = json.dumps(horoscopo)
			return result


if __name__ == "__main__":
	app.run()


