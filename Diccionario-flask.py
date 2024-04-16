from flask import Flask
app = Flask(__name__)


@app.route ('/')
def saludar():
    return 'Hola, esto es un dicionario de Slang Panameño!'


@app.route ('diccionario')
def diccionario(diccionario):
    return 'Birria: juego, Chuleta: sorpresa o admiracion, yalabetia: algo exagerado, mopri: primo de manera invertida'


@app.route('/hola/<nombre>')
def saludar_nombre(nombre):
    return 'Hola %s!' % nombre


if __name__ == '_main_':
    app.run()
