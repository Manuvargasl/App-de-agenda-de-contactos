import os
os.system("cls")

while True:
    print ("\t\t Mini Agenda de Contactos.\n")
    print ("1.  Agregar un contacto: nombre, teléfono, email.")
    print ("2.  Listar contactos: mostrar todos los contactos guardados.")
    print ("3.  Buscar un contacto por nombre.")
    print ("4.  Eliminar un contacto.")
    print ("5.  Salir del programa.\n")
    try:
        opcion = int(input("Elija una opcion.\n"))
        if opcion == 1:
            print("\t Agregar un contacto:")
        elif opcion == 2:
            print("\t Listar contactos:")
        elif opcion == 3:
            print("\t Buscar un contacto por nombre.")
        elif opcion == 4:
            print("\t Eliminar un contacto.")
        elif opcion == 5:
            print("\t Salir del programa.")
            print("Chao pecao'...")
            break
        else:
            print("La oipcion ingresada no exixte")
    except:
        print("Valor ingresado debe ser numerico")