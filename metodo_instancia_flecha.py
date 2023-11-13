""" Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas. """
import os

class Personaje:
    def __init__(self, nombre, cantidad_flechas):
        self.nombre = nombre
        self.cantidad_flechas = cantidad_flechas

    def info(self):
        print(f"{self.nombre} tiene {self.cantidad_flechas} flechas.")

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        print(f"{self.nombre} lanzó una flecha.")

def limpiar_consola():
    if os.name == "nt":
        os.system("cls")


limpiar_consola()
# Crear una instancia de la clase Personaje
arquero = Personaje(nombre="Legolas", cantidad_flechas=10)

# Información inicial
arquero.info()  # Legolas tiene 10 flechas.

# Llamar al método de instancia lanzar_flecha
arquero.lanzar_flecha()

# Información después de lanzar una flecha
arquero.info()  # Legolas tiene 9 flechas.
