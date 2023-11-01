import openai
openai.api_key = "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"

Interrogante = "Compara si la idea principal de las siguientes frases son similares entre si y retorna una respuesta en verdadero o falso y el porque de la respuesta: "
TextA = "1: messi fichara por el barsa mañana"
TextB = "2: el barcelona se reunira con messi para finalizar su fichaje, esto se realizara el dia de mañana"
PreguntaGPT = Interrogante + " " + TextA + " " + TextB 

def ValidarNoticia ():
    Pregunta = openai.Completion.create(engine="text-davinci-003",
                        prompt= PreguntaGPT,
                        max_tokens=2046)
    respuesta = Pregunta.choices[0].text
    print (respuesta)
    return respuesta

ValidarNoticia() 