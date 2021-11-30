import modelo
import vista
import os

class CONTROLADOR:

    def __init__(self):
        pass



mod = modelo.ABMC()

mod.crear_bd()

os.system("clear")




if __name__ == "__main__":
    vista.PANTALLA().menu_principal()
    
