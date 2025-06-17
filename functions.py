import os, time
# Trabajo Colaborativo: "Mini Agenda de Contactos"
# Objetivo:
# Desarrollar una pequeña aplicación de consola en Python que funcione como una agenda de contactos. El objetivo es aplicar los conocimientos de programación estructurada (variables, constantes, tipos de datos, estructuras de control, funciones, etc.) y prácticas básicas de trabajo colaborativo con Git y GitHub.
# ________________________________________
# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.


contactos = []
def agregar_usuario():
    nombre = ""
    while len(nombre) < 3:
        nombre = input("Ingrese el nombre del contacto:\n")
    contactos.append(nombre)
    print("nombre agregado con éxito!")

    
    telefono = ""
    while len(telefono) < 9:

        telefono = input("Ingrese el teléfono con los 9 dígitos:\n")

    print("Número ingresado con éxito")
    contactos.append(telefono)
    email = ""
    while len(email) < 5:
        email = input("Ingrese el correo electrónico. Debe tener un @\n")
    print("email agregado con éxito")
    contactos.append(email)
    print(contactos)
    time.sleep(3)


def listar_contacto():
    for x in range(len(contactos)):
        print(contactos[x])
    time.sleep(2)
    
    
    
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa