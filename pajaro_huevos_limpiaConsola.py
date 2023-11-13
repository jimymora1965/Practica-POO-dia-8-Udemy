import os

class Pajaro:
    alas = True

    def __init__(self, tipo, color):
        self.t = tipo
        self.c = color

    @classmethod
    def volar(cls):
        print(f"Las aves tienen alas: {cls.alas}")

    def cantidad_huevos(self):
        if self.t == "Canario":
            return 3
        else:
            return "Desconocido"

# Limpiar la consola
def limpiar_consola():
    if os.name == 'nt':
        # Windows
        os.system('cls')

# Crear una instancia de la clase Pajaro
piolin = Pajaro(tipo="Canario", color="Amarillo")

# Limpiar la consola
limpiar_consola()

# Llamar al método estático 'volar'
piolin.volar()

# Llamar al método 'cantidad_huevos' e imprimir el resultado
print(f"{piolin.t} pone {piolin.cantidad_huevos()} huevos")
