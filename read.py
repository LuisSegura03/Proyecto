import openai
import pymongo

MONGO_HOST="localhost" 
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PUERTO + "/"

openai.api_key = "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"
parabraClave = "Genera un resumen del contenido de esta pagina el resumen generado no debe tener comillas:"
url = ""
consulta = parabraClave + url

def leerNoticia ():
    Pregunta = openai.Completion.create(engine="text-davinci-003",
                        prompt=consulta,
                        max_tokens=2048)
    respuesta = Pregunta.choices[0].text
    print (respuesta)
    print (url)
    return respuesta

leerNoticia() 

