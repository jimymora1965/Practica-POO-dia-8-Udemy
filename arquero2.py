import os

class Arquero:
    def __init__(self,nombre, cantidad_flechas):
        self.n = nombre
        self.cf = cantidad_flechas

    
    def datos_generales(self):
        print(f"{self.n} tiene {self.cf} flechas")


    def total_flechas(self):
        self.cf = self.cf -1
        print(f"{self.n} lanzo una flecha")

def limpiar_consola():
    if os.name == "nt":
        os.system("cls")

limpiar_consola()
arquero = Arquero(nombre= "Legolas", cantidad_flechas= 10)
arquero.datos_generales()
arquero.total_flechas()
arquero.datos_generales()


