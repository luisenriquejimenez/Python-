#!/usr/bin/python

import sqlite3
import os 

APP_PATH = os.getcwd()
DB_PATH = APP_PATH+'/slangpanameño.db'

conn = sqlite3.connect(DB_PATH)
print ( "Conectado a la base de datos. ")

conn.execute('''CREATE TABLE 
        Dicionario (xopa, mopri, ofi, frio, ayalavida )''')
print("Dicionario creado.")


opcion = 0

print("""
¿Qué quieres hacer?
a) Agregar nueva palabra
c) Editar palabra existente
d) Eliminar palabra existente
e) Ver listado de palabras
f) Buscar significado de palabra
g) Salir
""")

opcion = int(input("Introduce una opcion: ") )     

if opcion == 1:
    print("Ingrese la palabra que desea agregar:")
elif opcion == 2:
    print("Ingreese la palabra que desea editar:")
elif opcion == 3:
    print("Ingrese la palabra que desea eliminar:")
elif opcion == 4:
        print("El listado de palabras es:") 
elif opcion == 5:
        print("Ingrese la palabra para ver su significade:")                  
else:
    print("Opción incorrecta")


conn.close()
