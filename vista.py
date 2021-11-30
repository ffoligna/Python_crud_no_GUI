import main
import sys
import os

class PANTALLA:

    def __init__(self):
        pass

    def menu_principal(self):

    # Pantalla principal del menú
        while True:
            menu = input(
            """
##########################################

Bienvenido al menu principal de la agenda!

    0) Salir
    1) Añadir contacto
    2) Lista de contactos
    3) Buscar contacto por ID
    4) Modificar contacto
    5) Eliminar contacto

##########################################
            
Elija una opción del 0 al 5:
>_ """)

            while menu not in ["0", "1", "2", "3", "4", "5"]:
                os.system("clear")
                print("Por favor, ingrese un número del 0 al 5.")
                menu = input(
        """
##########################################

Bienvenido al menu principal de la agenda!

    0) Salir
    1) Añadir contacto
    2) Lista de contactos
    3) Buscar contacto por ID
    4) Modificar contacto
    5) Eliminar contacto

##########################################
        
Elija una opción del 0 al 5:
>_ """)

    # Salir del menú
            if menu == "0":
                os.system("clear")
                print("""
#############################
Usted ha cerrado el programa.
#############################
    """)
                sys.exit()


    # Añadir contacto        
            elif menu == "1":
                os.system("clear")
                nombre = input("Ingrese un nombre: ")
                apellido = input("Ingrese un apellido: ")
                telefono = int(input("Ingrese un teléfono: "))
                main.mod.alta(nombre, apellido, telefono)
                print("""
###########################
Contacto añadido con éxito.
###########################
    """)
                PANTALLA().menu_principal()


    # Lista de contactos
            elif menu == "2":
                os.system("clear")
                print("### Lista de contactos ###")
                main.mod.listar_bd()
                PANTALLA().menu_principal()


    # Buscar contacto por ID 
            elif menu == "3":
                os.system("clear")
                main.mod.buscar_por_id(int(input("""
#########################################
Ingrese el ID para buscar el contacto: """)))
                PANTALLA().menu_principal()


    # Modificar contacto
            elif menu == "4":
                os.system("clear")
                main.mod.listar_bd()
                print("""
#########################################""")
                id = int(input("Ingrese el ID: "))
                nombre = input("Ingrese un nombre: ")
                apellido = input("Ingrese un apellido: ")
                telefono = int(input("Ingrese un teléfono: "))
                main.mod.modificacion(id, nombre, apellido, telefono)
                print("""
##############################
Contacto modificado con éxito.
##############################
""")
                PANTALLA().menu_principal()


    # Eliminar contacto    
            elif menu == "5":
                os.system("clear")
                main.mod.listar_bd()
                main.mod.baja(int(input("""
#########################################
Ingrese el ID para eliminar el contacto: """)))
                os.system("clear")
                print("""
#############################
Contacto eliminado con éxito.
#############################""")
                PANTALLA().menu_principal()








if __name__ == "__main__":
    PANTALLA().menu_principal()