#!/usr/bin/python

import sqlite3
import sys
import os 

def agregar_articulo ():
    os.system("cls")

    print("**Agregar articulo**")
    print("")


    codigo = input("Ingrese el codigo del articulo:")
    nombre = input("Ingrese el nombre del ariculo:")
    precio = input("Ingrese el precio del articulo: ")
    cantidad = input("Ingrese la cantidad de articulos: ")

    con = sqlite3.connect("articulo.db")
    cursor = con.cursor()
    cursor.execute("insert into articulos (nombre,precio.cantidad) values('"+nombre+"'+'"+precio+"'+'"+cantidad+")")
    con.commit()
    con.close()

    print("articulo agregado exitosamente!")
    print("")
    print("[6] volver al menu.")
    print("[5] salir.")

    opcion = input("Elija una opcion: ")

    if opcion == "6":
        menu()
    elif opcion == "5":
        sys.exit()


def ver_articulo():
    os.system("cls")

    print("**Ver articulo**")
    print("")

    con = sqlite3.connect("articulo.db")
    cursor = con.cursor()
    cursor.execute("select * from articulo")

print("------\t\t------\t\t----------\t\t------\t\t----\t\t----\t\t------------")
print("Codigo\t\tNombre\t\tprecio\t\tcantidad")
print("------\t\t------\t\t----------\t\t------\t\t----\t\t----\t\t------------")


for articulo in cursor:
    print(articulo[1]+"\t\t"+articulo[2]+"\t\t"+articulo[3]+"\t\t"+articulo[4]+"\t\t"+articulo[5]+"\t\t"+articulo[6]+"\t\t"+articulo[7])
    print("")
con.close()

print("Revision de los articulo ")
print("Articulos verificador.")
print("[6] volver al menu.")
print("[5] salir.")


opcion = input("Elija una opcion: ")

if opcion == "6":
    menu()
elif opcion == "5":
    sys.exit()


def modificar_articulo():
    os.system("cls")
    con = sqlite3.connect("articulo.db")
    cursor = con.cursor()
    cursor.execute("select * from articulo")

    print("**Modificar producto**")
    print("")

    print("------\t\t------\t\t----------\t\t------\t\t----\t\t----\t\t------------")
    print("Codigo\t\tNombre\t\tprecio\t\tcantidad")
    print("------\t\t------\t\t----------\t\t------\t\t----\t\t----\t\t------------")
    print("")

    for articulo in cursor:
        print(str(articulo[1]+"\t\t"+articulo[2]+"\t\t"+articulo[3]+"\t\t"+articulo[4]+"\t\t"+articulo[5]+"\t\t"+articulo[6]+"\t\t"+articulo[7]))
        print("")


        print("")
        codigo = input("Ingrese el codigo del articulo a modificar:")

        print("")
        nombre = input("Ingrese el nombre del nuevo alticulo:")
        precio = input("Ingrese el precio del nuevo articulo:")
        cantidad = input("Ingrese la cantidad del nuevo producto:")

        sql = "updat earticulo set nombre='"+nombre+"',precio='"+precio+"',cantidad='"+cantidad+"" 
        cursor.execute(sql)
        con.commit()
        con.close()

        print("Articulo modificado exitossmente!")
        print("")
        print("[6] volver al menu.")
        print("[5] salir.")


opcion = input("Elija una opcion: ")

if opcion == "6":
    menu()
elif opcion == "5":
    sys.exit()


def eliminar_articulo():
    os.system("cls")
    con = sqlite3.connect("articulo.db")
    cursor = con.cursor()
    cursor.execute("select * from articulo")


    print("**Eliminar articulo**")
    print("")
    print("------\t\t------\t\t----------\t\t------\t\t----\t\t----\t\t------------")
    print("Codigo\t\tNombre\t\tprecio\t\tcantidad")
    print("------\t\t------\t\t----------\t\t------\t\t----\t\t----\t\t------------")
    print("")


    for articulo in cursor:
        print(str(articulo[1]+"\t\t"+articulo[2]+"\t\t"+articulo[3]+"\t\t"+articulo[4]+"\t\t"+articulo[5]+"\t\t"+articulo[6]+"\t\t"+articulo[7]))
        print("")

    print("")
    codigo = input("Ingrese el codigo del articulo a eliminar:")

    sql = "delete from articulo where codigo="+codigo

    cursor.execute(sql)
    con.commit()
    con.close()

    print("Eliminacion de articulo realizada!")
    print("")
    print("[6] volver al menu.")
    print("[5] salir.")


opcion = input("Elija una opcion: ")

if opcion == "6":
    menu()
elif opcion == "5":
    sys.exit()


def menu():
    os.system("cls")
    print("**Informacion de articulos**")
    print("")
    print("[1] Agregar articulo:")
    print("[2] Ver articulo")
    print("[3] Modificar articulo")
    print("[4] Eliminar articulo")
    print("[5] Salir ")

    opcion = input("Elija una opcion:")

    if opcion == "1":
        agregar_articulo()
    elif opcion == "2":
        ver_articulo()
    elif opcion =="3":
        modificar_articulo()
    elif opcion =="4":
        eliminar_articulo()
    elif opcion =="5":
        sys.exit()
    else:
        opcion = input("Ingresaste una opcion incorrecta.")
        menu(opcion)
menu() 
