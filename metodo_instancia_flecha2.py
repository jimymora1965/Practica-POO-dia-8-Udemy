# Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
import os
class Personaje:
    
    def __init__(self, nombre, cantidad_flechas):
        self.n = nombre
        self.cf = cantidad_flechas
        
    def info(self):
        print(f"{self.n} tiene {self.cf} flechas")
        
    def lanzar_flecha(self):
        self.cf = self.cf - 1
        print(f"{self.n} lanzo una flecha")

def limpiar_consola():
    if os.name =="nt":
        os.system = ("cls")
        
limpiar_consola()       
arquero = Personaje(nombre = "Jimy", cantidad_flechas = 10)
arquero.info()
arquero.lanzar_flecha()
arquero.info()