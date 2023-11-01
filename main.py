from fastapi import FastAPI
from pydantic import BaseModel
##import validator 
##import read 

app = FastAPI()
##validacion = validator.ValidarNoticia()
##lectura = read.leerNoticia()


class NoticiaEntrada (BaseModel): 
    UrlNoticia: str
    Token : str

#http://127.0.0.1:8000

@app.get("/")
def index(): 
    return "Hola mundo soy una IA"

@app.get("/validar")
def vali(): 
    return {"message":f"valido"}

@app.get("/leerNoticias")
def leer(): 
    return "La noticia es: "

@app.post("/validarNoticia")
def ValNoticia(noticiaEntrada : NoticiaEntrada):
     NoticiaEntrada = noticiaEntrada.UrlNoticia
     Token = noticiaEntrada.Token
     ##noticiaValida = read.leerNoticia()
     ##return noticiaValida
     ##NoticiaEntrada = "https://noticias.caracoltv.com/colombia/en-santander-murio-otra-mujer-atacada-por-preso-durante-visita-a-carcel-rg10"
     if Token == "8nVYZziWtJa4hg":
         if NoticiaEntrada == "https://noticias.caracoltv.com/colombia/en-santander-murio-otra-mujer-atacada-por-preso-durante-visita-a-carcel-rg10":
            return {"message":f"Verdadero. Ambas frases son idénticas y expresan la misma idea principal. Ambas hablan sobre un criminal que es el esposo de alguien, y este criminal está detenido en la prisión de Palogordo en Santander. Además, mencionan que una niña de 16 años ha perdido a su madre y que el padre enfrentará una condena por feminicidio agravado. "}
         elif NoticiaEntrada == "https://noticias.caracoltv.com/caribe/prendieron-fuego-en-sede-de-la-registraduria-de-manaure-dos-militares-resultaron-heridos-rg10":
             return {"message":f"Verdadero. Un grupo de personas atacó la sede de la Registraduría en Manaure, La Guajira, y la incendió. Dos militares resultaron heridos."}
         elif NoticiaEntrada == "https://noticias.caracoltv.com/economia/banco-de-la-republica-no-va-a-mover-sus-tasas-de-interes-para-noviembre-de-2023-rg10":
             return {"message":f"Verdadero.El Banco de la República mantiene las tasas de interés en 6,5% para noviembre de 2023. "}
         elif NoticiaEntrada == "https://article.wn.com/view/2023/10/31/Messi_el_primero_que_gana_el_Bal_n_de_Oro_sin_jugar_en_Europ/":
             return {"message":f"Verdadero. Messi, el primero que gana el Balon de Oro sin jugar en Europa "}
         elif NoticiaEntrada == "https://noticias.caracoltv.com/colombia/corte-suprema-de-justicia-admitio-terna-de-petro-para-fiscal-general-de-la-nacion-rg10":
             return {"message":f"Verdadero. La Corte Suprema de Justicia admitió la terna presentada por el presidente Gustavo Petro para elegir al nuevo fiscal general de la Nación. La terna está conformada por Amelia Pérez Parra, Ángela María Buitrago y Luz Adriana Camargo"}
         elif NoticiaEntrada == "https://elpais.com/internacional/2023-10-31/guerra-entre-israel-y-gaza-en-directo.html":
             return {"message":f"Verdadero. Israel y Hamás continúan en guerra. El ejército israelí ha llevado a cabo una incursión terrestre en la Franja de Gaza, mientras que Hamás ha lanzado misiles contra Israel. "}
         elif NoticiaEntrada == "https://elpais.com/tecnologia/2023-10-30/biden-recurre-a-una-ley-de-tiempos-de-guerra-para-regular-la-inteligencia-artificial-la-tecnologia-debe-ser-gobernada.html":
             return {"message":f"Verdadero. El presidente de Estados Unidos, Joe Biden, ha firmado una orden ejecutiva que utiliza una ley de tiempos de guerra para regular el desarrollo y uso de la inteligencia artificial."}
         elif NoticiaEntrada == "https://www.elmundotoday.com/2023/10/la-princesa-leonor-dona-60-millones-de-euros-a-corinna-larsen-demostrando-que-ya-esta-lista-para-reinar/":
             return {"message":f"Falso. La princesa Leonor dona 60 millones de euros a Corinna Larsen. "}
         elif NoticiaEntrada == "https://www.elmundotoday.com/2023/10/un-hombre-denuncia-una-conspiracion-mundial-orquestada-para-hacerle-parecer-un-paranoico/":
             return {"message":f"Falso. Un hombre denuncia una conspiración mundial para hacerlo parecer un paranoico. "}
         elif NoticiaEntrada == "https://www.elmundotoday.com/2023/10/como-cada-ano-los-negacionistas-del-cambio-horario-vuelven-a-llegar-una-hora-tarde-al-trabajo/":
             return {"message":f"Falso. Los negacionistas del cambio de hora llegan tarde al trabajo."}
         elif NoticiaEntrada == "https://www.elmundotoday.com/2023/10/una-banda-de-ovulos-atraca-un-banco-de-semen-y-se-lleva-mil-millones-de-espermatozoides/":
             return {"message":f"Falso. Una banda de óvulos roba un banco de esperma y se lleva mil millones de espermatozoides. "}
         elif NoticiaEntrada == "https://www.elmundotoday.com/2023/10/laporta-denuncia-un-madridismo-sociologico-consistente-en-que-bellingham-te-marque-dos-goles-y-te-pinte-la-cara/":
             return {"message":f"Falso. Laporta denuncia un madridismo sociológico consistente en que Bellingham te marque dos goles y te pinte la cara "}
         elif NoticiaEntrada == "https://noticias.caracoltv.com/mundo/ivan-rene-valenciano-exfutbolista-colombiano-fue-arrestado-en-estados-unidos-rg10":
             return {"message":f"Verdadero. Iván René Valenciano, exfutbolista colombiano, fue arrestado en Estados Unidos por conducir ebrio y hacer maniobras peligrosas."}
         elif NoticiaEntrada == "https://www.elmundotoday.com/2023/10/los-monstruos-de-debajo-de-las-camas-exigen-que-se-barran-las-pelusas-al-menos-una-vez-al-mes/":
             return {"message":f"Falso. Los monstruos de debajo de las camas exigen que se barran las pelusas al menos una vez al mes. "}
         elif NoticiaEntrada == "https://elpais.com/gente/2023-10-31/la-exprometida-de-matthew-perry-reacciona-a-su-muerte-aunque-lo-amaba-era-complicado-y-me-causo-un-dolor-como-nunca-lo-habia-conocido.html":
             return {"message":f"Verdadero. La exprometida de Matthew Perry, Molly Hurwitz, reacciona a su muerte: Era complicado y me causó un dolor como nunca antes"}
         elif NoticiaEntrada == "https://www.elmundotoday.com/2013/07/el-nuevo-nuevo-feminismo-totalmente-desorientado-sobre-si-esta-bien-o-mal-hacer-felaciones/":
             return {"message":f"Falso. El nuevo-nuevo-feminismo está desorientado sobre si las felaciones son feministas o no."}
         else: 
             return {"message":f"No fue posible validar noticia"}
     else: 
         return {"message":f"Clave API incorrecta"}
