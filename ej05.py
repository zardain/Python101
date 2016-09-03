# -*- coding: utf-8 -*-
#Se debera generar un sistema que mantenga en memoria datos de una agenda.
#    - El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
#    agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
#    editar, permite modificar cualquiera de los contactos seleccionando su email.
#    borrar, elimina un contacto.

if __name__ == "__main__":
    flagSalida = False
    listaAgenda = []
    dicPersona = {}

    while(flagSalida==False):
            print("*****************************")
            print("*** Agenda de Contactos *****")
            print("*****************************")
            print(" ")
            print("OPCIONES")
            print("             --> Agregar (1) ")
            print("             --> Editar (2) ")
            print("             --> Borrar (3) ")
            print("             --> Mostrar (4) ")
            print("             --> Salir (5) ")
            print(" ")

            opciones = int(raw_input("Ingrese alguna opción: "))

            #agregar
            if opciones == 1:
                dicPersona["email"] = raw_input("Ingrese Email: ")
                dicPersona["telefono"] = raw_input("Ingrese Telefono: ")
                dicPersona["nombre"] = raw_input("Ingrese Nombre: ")
                dicPersona["domicilio"] = raw_input("Ingrese Domicilio: ")
                dicPersona["edad"] = raw_input("Ingrese Edad: ")
                dicPersona["dni"] = raw_input("Ingrese DNI: ")

                listaAgenda.append(dicPersona)
            #editar
            elif opciones == 2:
                print("Contactos Disponibles")
                indice = 0
                for contacto in listaAgenda:
                    print("Nombre: " + contacto["nombre"] + "(" + indice + ")")
                    indice += 1
                indiceContacto = raw_input("Elija un numero de contacto: ")
                contactoAux = listaAgenda[indiceContacto]

                contactoAux["email"] = raw_input("Ingrese Email: ")
                contactoAux["telefono"] = raw_input("Ingrese Telefono: ")
                contactoAux["nombre"] = raw_input("Ingrese Nombre: ")
                contactoAux["domicilio"] = raw_input("Ingrese Domicilio: ")
                contactoAux["edad"] = raw_input("Ingrese Edad: ")
                contactoAux["dni"] = raw_input("Ingrese DNI: ")

                listaAgenda.insert(indiceContacto,contactoAux)
            #mostrar
            elif opciones == 4:
                print("Contactos Disponibles")
                indice = 0
                for contacto in listaAgenda:
                    print("Nombre: " + contacto["nombre"] + " (" + str(indice) + ")")
                    indice += 1

            continuar = raw_input("Desea Continuar? (y,n)")
            if continuar == "n":
                flagSalida = True
