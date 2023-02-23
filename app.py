from flask import Flask, render_template # importamos Flask y render_template
import requests

app = Flask(__name__) # Creamos aplicacion de Flask
# Basicamente lo que hace la linea 3 es decirle a flask que use este archivo como aplicacion  

@app.route('/') # Extendemos la aplicacion agregando una nueva ruta (ruta principal)
def index():
    return 'Hello world'

@app.route('/nombre/<contrasenha>')
def contrasena(contrasenha):
    if contrasenha == '123':
        return 'Accediste'
    else:
        return 'Quien sos'

@app.route('/<nombre>/<contrasenha>')
def nombre_contrasenha(nombre, contrasenha):
    if contrasenha == "123":
        return f"Bienvenido {nombre}"       
    else:
        return f"Quien sos {nombre}??"

@app.route('/hola')
def hola():
    return """
    <h1>Hola, me llamo marcelo</h1>
    <p>Esta es mi primera pagina web</p>
    <p>Estoy en el taller web</p>
    """

@app.route('/tarjeta')
def tarjeta():

    nombre = 'Pablito'
    descripcion = 'Pinguino Fachero'
    titulo_ubicacion = 'Ultima ubicacion conocida'
    ubicacion = 'Arsenal Cue'
    imagen_url = 'https://pbs.twimg.com/media/EzS3G6rUcAcfWVq.jpg'

    return render_template('tarjeta.html', nombre=nombre, descripcion=descripcion, titulo_ubicacion=titulo_ubicacion, ubicacion=ubicacion, imagen_url=imagen_url)

# Ruta personaje estatico
@app.route('/personaje')
def personaje():
    # Definimos la URL a la cual vamos a hacer la peticion
    url = 'https://rickandmortyapi.com/api/character/2'

    # Hacemos la peticion a la API y convertimos el JSON a un diccionario
    personaje = requests.get(url).json()

    # Extraemos los datos que necesitamos del diccionario
    nombre = personaje['name']
    estado = personaje['status']
    especie = personaje['species']
    ubicacion = personaje['location']['name']
    imagen_url = personaje['image']
    # Creamos descripcion a partir de especie y estado
    descripcion = especie + ' ' + estado
    # Definimos el titulo_ubicacion
    titulo_ubicacion = 'Ultima ubicacion conocida'
 
    return render_template('personaje.html', nombre=nombre, descripcion=descripcion, titulo_ubicacion=titulo_ubicacion, ubicacion=ubicacion, imagen_url=imagen_url)

# Ruta personaje dinamico
@app.route('/personaje/<id>')
def personaje_dinamico(id):
    # Definimos la URL a la cual vamos a hacer la peticion
    url = f'https://rickandmortyapi.com/api/character/{id}'

    # Hacemos la peticion a la API y convertimos el JSON a un diccionario
    personaje = requests.get(url).json()

    # Extraemos los datos que necesitamos del diccionario
    nombre = personaje['name']
    estado = personaje['status']
    especie = personaje['species']
    ubicacion = personaje['location']['name']
    imagen_url = personaje['image']
    # Creamos descripcion a partir de especie y estado
    descripcion = especie + ' ' + estado
    # Definimos el titulo_ubicacion
    titulo_ubicacion = 'Ultima ubicacion conocida'
 

    return render_template('personaje.html', nombre=nombre, descripcion=descripcion, titulo_ubicacion=titulo_ubicacion, ubicacion=ubicacion, imagen_url=imagen_url)

@app.route('/lista_personajes')
def lista_personajes():

    # Definimos la URL a la cual vamos a hacer la peticion
    url = 'https://rickandmortyapi.com/api/character'

    # Hacemos la peticion a la API y convertimos el JSON a un diccionario
    respuesta = requests.get(url).json()

    # Accedemos a la lista de personajes de la respuesta
    lista_personajes = respuesta['results']

    return render_template('lista_personajes.html', lista_personajes=lista_personajes)

if __name__ == '__main__': 
    app.run(debug=True)

    


 