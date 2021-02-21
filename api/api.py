import web
import json
import random


carta = {}
urls = (
    '/(.*)',
    'Carta',
)
app = web.application(urls, globals())

class Carta():
  def __init__(self):
    pass
    
    
  def GET(self, carta_astral):
    try:
      fech_dia = int(carta_astral[0:2])
      fech_mes = int(carta_astral[3:5])
      print(fech_dia, fech_mes)
      
      
      if fech_dia >= 21 and fech_mes == 1 or fech_mes == 2 and fech_dia <= 19:
        horoscopo = {}
        horoscopo["Nombre"] = "Acuario"
        horoscopo["Fecha"] = "Enero  21 – Febrero 19"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "7, 14 y 20"
        horoscopo["Color"] = "Gris, azul y verde"
        horoscopo["Horóscopo del día"] =(random.choice([ "Estarás inexplicablemente tenso, pese a las mil y una bondades que te reserva la jornada. No olvides que todo pasa.","Estás pasando por un momento un poco inexplicable, Acuario, como si tu planeta regente se hubiera eclipsado. Parece que tienes falta de confianza en ti misma a diario y estás con la autoestima un poco por los suelos. Has dejado de valorar tu talento quizá a raíz de un contratiempo sin importancia. Hoy intenta recuperar la seguridad y convéncete de que tienes capacidad de sobra para llevar a cabo cualquier tema que se te encomiende.", "Te costará bastante que tus impulsos sean más moderados. Y por ello deberías mantener tus vacilaciones, hasta un momento en el que sientas mayor seguridad para llevar a adelante lo que tienes planificado para este día.","Hoy prodigarás y recibirás innumerables expresiones de afecto. La energía del día es propicia para las buenas comunicaciones, la armonía y el bienestar. Por ello, tú y los demás sentirán la necesidad de expresar lo que sienten mutuamente. Aprovecha para decirles a las personas especiales en tu vida lo que sientes por ellas. Es hora de que lo hagas y no necesitas una ocasión especial para demostrarles tu aprecio."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 20  and fech_mes == 2 or fech_mes == 3 and fech_dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Picis"
        horoscopo["Fecha"] = "Febrero  20 – Marzo 20"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "75, 11 y 19"
        horoscopo["Color"] = "Verde, azul y morado."
        horoscopo["Horóscopo del día"] = (random.choice([ "Escucha una propuesta que rompe con tus prejuicios. Un elogio llega desde el lugar menos esperado. No lo descartes.","Hoy tu gran desafío estará relacionado con la manera en la que llevas a cabo tus prioridades", "Sentirás que necesitas poner tu vitalidad y profundidad, y especialmente tus percepciones, al servicio de tus obras y de tus actuaciones. Y por ello lo más importante es que utilices tu ecuanimidad y tu equilibrio para que tu entorno y tu forma de sentir sea equilibrado y más armónico.","Hoy tus capacidades psíquicas van a estar presentes con mucha fuerza. Siempre tuviste una parte intuitiva, y hoy esos sentidos extras estarán elevados. Podrás anticipar lo que alguien dirá o hará. ¡O podrás saber quién te llamará por teléfono antes de que suene! Quizás experimentes graciosas coincidencias, como por ejemplo estar pensando en alguien justo antes de encontrártelo"]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 21  and fech_mes == 3 or fech_mes == 4 and fech_dia <= 19:
        horoscopo = {}
        horoscopo["Nombre"] = "Aries"
        horoscopo["Fecha"] = "Marzo  21 – Abril 19"
        horoscopo["Elemento"] = "Fuego"
        horoscopo["Numero de la suerte"] = " 7, 17 y 21."
        horoscopo["Color"] = "Gris, azul y verde"
        horoscopo["Horóscopo del día"] = (random.choice(["Contarás con una energía potenciada para encarar los cambios que tanto deseas. Te adaptarás a los tiempos que se avecinan.","Es un día para tener mayor tranquilidad y mantener la lengua a buen recaudo para evitar la ironía imperfecta. Evita sobrecargar tu sistema nervioso. Planifica tus actuaciones con bastante tiempo y separando unas actividades de otras; ya que así dedicarás el tiempo preciso a cada una.","Será un día en el que te sentirás con mucho entusiasmo, y esta gran vitalidad te llevará ejecutar un montón de proyectos que tenías pendientes. Como te moverás con una gran actividad deberás mantener la calma y la paciencia con personas más lentas que tú. Deberás dedicarte más tiempo a trabajar individualmente y a sacar tus ideas adelante."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 20  and fech_mes == 4 or fech_mes == 5 and fech_dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Tauro"
        horoscopo["Fecha"] = "Abril  20 – Mayo 20"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = "4, 6 y 11."
        horoscopo["Color"] = "Verde claro, rosa y turquesa."
        horoscopo["Horóscopo del día"] = (random.choice(["Para encontrar la solución, separa cada cosa y analiza cada plano. Sentirás todo el apoyo familiar y de tu entorno más cercano.","Necesitas sentirte libre e ir a tu aire. Y tú estado positivo y alegre atraerá a otras personas que también se sientan de esa manera. Así que, lo más importante es que te sientas bien. Olvida las críticas o pensar qué es lo que has hecho mal. Lo importante es comenzar de cero, y así introducirás un revulsivo en tu vida.", "Recapacitarás en un área de tu vida que siempre es proclive a los cambios de humor y a la inestabilidad; y se refiere a las relaciones con los demás, y especialmente a las de pareja. Te gusta ir a tu aire y con un gran sentido de la libertad, pero a veces tienes que intentar flexibilizar posturas y ajustarte también a los demás."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 21  and fech_mes == 5 or fech_mes == 6 and fech_dia <= 21:
        horoscopo = {}
        horoscopo["Nombre"] = "Géminis"
        horoscopo["Fecha"] = "Mayo  21 – Junio 21"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "2, 4, 7 y 9"
        horoscopo["Color"] = "Azul, violeta y amarillo"
        horoscopo["Horóscopo del día"] = (random.choice(["Mientras tú quieres hacer un balance y cerrar una etapa surgirán otras alternativas y nuevos caminos para recorrer.","Hoy sentirás que necesitas mayor tranquilidad y que tus pensamientos fluyan más lentamente, e inclusive que paren. Ese es el estado perfecto. Podrás ocuparte con calma de cada pequeño asunto que trates. Y por eso es importante que utilices el razonamiento y a la vez la percepción sutil; ya que podrás combinar ambos","Estás en un día importante en el cual te plantearás nuevas metas qué tienen visos de salir adelante y de ser fructíferas. Pero para ello necesitas vigilar tus pensamientos para evitar una crítica en exceso, tanto en tus actuaciones como en las de los otros. Así que fluye como una hoja a través del río y déjate llevar por tu naturaleza bondadosa y altruista."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 20  and fech_mes == 6 or fech_mes == 7 and fech_dia <= 20:
        horoscopo = {}
        horoscopo["Nombre"] = "Cáncer"
        horoscopo["Fecha"] = "Junio  20 – Julio 20"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "5, 6, 8 y 19."
        horoscopo["Color"] = "Blanco, plateado y verde"
        horoscopo["Horóscopo del día"] = (random.choice(["Hoy tendrás un muy buen día, en el que las buenas noticias podrían llegar cuando menos lo imagines. Debes aprovechar el momento.","Muchas personas te pedirán favores urgentes, y como de costumbre, aceptarás ayudarlos. Por lo general puedes manejarlo bien, pero hoy tal vez excedan tus posibilidades. Deberás correr todo el día para cumplir tus compromisos. Detente un momento, y observa todo en su justa dimensión.","Ciertas condiciones peligrosas en casa podrían provocar accidentes si no se rectifican. Como algunas no son muy obvias, advierte a tus familiares que tengan cuidado. Hoy no conviene que se haga ningún tipo de trabajo pesado en casa. Si pensabas hacer reparaciones de consideración sería mejor que pospongas tus planes. Como estás muy metódico, hoy es el día ideal para planificar dichas reparaciones."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 22  and fech_mes == 7 or fech_mes == 8 and fech_dia <= 22:
        horoscopo = {}
        horoscopo["Nombre"] = "Leo"
        horoscopo["Fecha"] = "Julio  22 – Agosto 22"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "1, 9, 10."
        horoscopo["Color"] = "Dorado, naranja y verde."
        horoscopo["Horóscopo del día"] = (random.choice(["Tu capacidad de entrega a los problemas ajenos aumenta cada día. Tendrás mucha decisión para ayudar. Serás recompensado.","Hoy quizás intentes aprender los últimos avances tecnológicos, seguramente relacionados con la computación, y puede que lo encuentres muy confuso. Tu mente puede estar a punto de 'sobrecargarse', así que probablemente lo mejor sea ir paso a paso y ¡tomarse las cosas con más calma! También es importante que no olvides tomarte recreos y despejar tu mente. Si intentas incorporar demasiada información a la vez, seguramente dé como resultado que no puedas asimilar ni siquiera un poco.","Hoy te preocupa un miembro de tu familia. Esta persona podría estar muy nerviosa por el trabajo, dinero, o posiblemente por un amorío que ha terminado. Di cualquier palabra confortante que te salga, pero no esperes que te responda, y no caigas en la trampa de pensar que tus dulces palabras fueron dichas en vano. Sí registró. Es sólo que le va a llevar un tiempo para aceptar la situación."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 23  and fech_mes == 8 or fech_mes == 9 and fech_dia <= 22:
        horoscopo = {}
        horoscopo["Nombre"] = "Virgo"
        horoscopo["Fecha"] = "Agosto  23 – Septiembre 22"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = "10, 15 y 27."
        horoscopo["Color"] = "Blanco, violeta y naranja."
        horoscopo["Horóscopo del día"] = (random.choice(["Será mejor que comiences a planificar mejor tu vida, al menos en los aspectos básicos. No permitas que las cosas simplemente te sucedan.","Tus acciones y emociones saldrán de un sitio primario dentro tuyo, haciéndote actuar y reaccionar con instintos salvajes. Las palabras sonarán mordaces, por lo tanto sé cuidadoso/a en cómo las utilizas.","Estarás con humor de expresarte con audacia. Tu carisma y ardientes encantos serán hoy muy poderosos. Los que te rodean podrían sentirse un poco intimidados por la fuerza de tu personalidad, así que intenta no ser demasiado agresivo. Puedes encontrar la manera de hablar con claridad, sin herir los sentimientos de los demás. Concéntrate en usar tu energía de manera positiva y productiva. ¡Hoy podrás lograr cosas maravillosas!"]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 23  and fech_mes == 9 or fech_mes == 10 and fech_dia <= 22:
        horoscopo = {}
        horoscopo["Nombre"] = "Libra"
        horoscopo["Fecha"] = "Septiembre  23 – Octubre 22"
        horoscopo["Elemento"] = "Aire"
        horoscopo["Numero de la suerte"] = "2, 8, 19"
        horoscopo["Color"] = "Rosa, azul y verde."
        horoscopo["Horóscopo del día"] = (random.choice(["Período para el aprendizaje, el cambio de hábito y buscar nuevas oportunidades. Agenda tus citas de trabajo, evita contratiempos.","Hoy te espera un día muy agitado, trabajarás bien con otros grupos. Tu imaginación es tan activa que bien podrías estar viviendo escenas de tus sueños. Las personas de tu vida tienen un papel más importante que en el pasado. Demuéstrales tu aprecio y agradecimiento. Juntos podrán disipar cualquier duda que pueda empañar el día de hoy.","A causa de un pequeño conflicto entre tus obligaciones laborales y tus responsabilidades familiares o sentimentales, hoy podrías sentir cierta presión. Debes cuidar, que tus actitudes no varíen al compás de tu humor. Intenta ser coherente, de lo contrario se agravarán las frustraciones mutuas. Sin embargo, gracias a que hoy tu capacidad para asumir compromisos es muy alta, podrás salvar la situación. ¡Aprovéchala al máximo!"]))
        result= json.dumps(horoscopo)
        return result


      elif fech_dia >= 23 and fech_mes == 10 or fech_mes == 11 and fech_dia <= 21:
        horoscopo = {}
        horoscopo["Nombre"] = "Escorpio"
        horoscopo["Fecha"] = "Octubre  23 – Noviembre 21"
        horoscopo["Elemento"] = "Agua"
        horoscopo["Numero de la suerte"] = "4, 13 y 21."
        horoscopo["Color"] = "Rojo, verde y negro"
        horoscopo["Horóscopo del día"] = (random.choice(["Golpe de suerte. Buena fortuna en los negocios, el estudio, los viajes y los juegos de azar. Toma la iniciativa y triunfarás.","Recibirás información en tu entorno laboral que podría llevarte a considerar ciertas inversiones. Pero ten cuidado: no todo es tan bonito como parece. Espera un poco y, si te apetece, investiga por tu cuenta. Podrías tener algunos sueños interesantes que te inciten a estudiar algún tema específico, quizá relacionado con las ciencias o el ocultismo. Es probable que absorbas mucha información, así que, ¡adelante!","De alguna manera, te has convertido en el hombre con las respuestas. El problema de ser competente es que las personas suelen ir a ti para solucionar sus problemas. No los puedes culpar, pero debes mantenerte firme para decirles que no. No eres la mesa de ayuda para los amigos y familiares cuyas carreras flaquean y sus relaciones no son muy felices. Al negarles tu ayuda, le otorgas fuerzas para que busquen soluciones por si solos. Explícales que al negarle tu ayuda, a la larga los estás ayudando más."]))
        result= json.dumps(horoscopo)
        return result

      elif fech_dia >= 22  and fech_mes == 11 or fech_mes == 12 and  fech_dia <= 21:
        horoscopo = {}
        horoscopo["Nombre"] = "Sagitario"
        horoscopo["Fecha"] = "Noviembre  20 – Diciembre 20"
        horoscopo["Elemento"] = "Fuego"
        horoscopo["Numero de la suerte"] = " 3, 8, 13."
        horoscopo["Color"] = "Blanco, azul y verde."
        horoscopo["Horóscopo del día"] =  (random.choice(["Agresiones cruzadas te tendrán a mal traer. Pese a estar libre de las cadenas que te tenían atado habrá problemas sentimentales.","Deja que tu naturaleza ávida e inquieta se manifieste por otros medios que no sea la palabra. Demuestra tu cariño con una caricia leve o un abrazo reconfortante que dure un poco más de lo normal. Ese momento de silencio absoluto crea una conexión íntima, donde sobran las palabras. Sería bueno que establecieras esa conexión con las personas que más quieres.","Hoy estarás un poquito más irritable que de costumbre, y si no te controlas, podrías descargarte en tus amigos o en tu pareja. Esta irritación parece provenir de emociones reprimidas en el pasado, sin relación con tu vida presente. Trata de pensar antes de hablar. Pero no todo es negativo, hoy la pasión y la sensualidad se sumarán a tus encantos. ¡Organiza un encuentro romántico!","Hoy podrías actuar como guía o mentor de alguien. Si tienes hijos, puedes ayudarlos a aprender cómo se hace algo que les interese. Puedes ser su entrenador en alguna disciplina deportiva o guiarlos para que comprendan una relación. Hasta podrías ayudarlos a descubrir su vocación. Si no tienes hijos, alguno de tus sobrinos apreciará tus consejos."]))
        result= json.dumps(horoscopo)
        return result
          
      elif fech_dia >= 22 or fech_dia <= 20 and fech_mes == 12 or fech_mes == 1:
        horoscopo = {}
        horoscopo["Nombre"] = "Capricornio"
        horoscopo["Fecha"] = "Diciembre  22 – Enero 20"
        horoscopo["Elemento"] = "Tierra"
        horoscopo["Numero de la suerte"] = " 3, 6, 16."
        horoscopo["Color"] = "Negro, azul y marrón."
        horoscopo["Horóscopo del día"] = (random.choice(["El fruto de tu esfuerzo y perseverancia te permitirán comprar ropa, calzado, perfumes y accesorios necesarios para verte mejor.","Te concentras en tus hijos o sobrinos... para ti, la Navidad es ante todo una fiesta para los más jóvenes, este año y no hay duda de que sus ojos brillan menos porque es un momento complejo!","Te tomas la molestia de complacer a los que te rodean, tus dones están a la altura, tu ternura se extiende a tu alrededor y a cambio, no faltan las atenciones delicada","Hoy te darás cuenta que necesitas realizar cierta compra. Quizás tu casa o auto necesiten reparaciones importantes, o sea imprescindible un nuevo equipo para tu trabajo. Esto será muy poco motivante, ya que significará gastar dinero que preferirías utilizar para algo más emocionante, sin embargo, piensa en el beneficio que te acarreará este gasto, y lo prudente de la decisión. Si no posees el dinero ahora, piensa en ahorrar un poco."]))
        result= json.dumps(horoscopo)
        return result
    except:
      
      horoscopo = {}
      horoscopo["Fecha"] = "La fecha  " + str(carta_astral)
      horoscopo["Error"] = "Valor incorrecto"
      horoscopo["Solucion"] = "Ingresa la fecha de tu nacimiento formato DD/MM/AAAA"
      result= json.dumps(horoscopo)
      return result


if __name__ == "__main__":
	app.run()
