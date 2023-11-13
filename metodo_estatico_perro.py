class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre

    def info(self):
        print(f"Soy {self.nombre}, una mascota.")

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

# Crear una instancia de la clase Mascota
mi_mascota = Mascota(nombre="Firulais")

# Llamar al método de instancia info()
mi_mascota.info()

# Llamar al método estático respirar()
Mascota.respirar()
