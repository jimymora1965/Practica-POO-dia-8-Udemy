import os

class Flechas:
    def __init__(self, cantidad_inicial):
        self.cantidad_flechas = cantidad_inicial

    def cargar_flechas(self, cantidad):
        self.cantidad_flechas += cantidad
        print(f"Has cargado {cantidad} flechas y tienes {self.cantidad_flechas} disponibles")

    def disparar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print("Has lanzado una flecha")
        else:
            print("No tienes flechas para lanzar")

    def mostrar_flechas_disponibles(self):
        print(f"Tienes {self.cantidad_flechas} flechas disponibles")

def limpiar_consola():
    os.system('cls')

cantidad_inicial = int(input("Ingresa la cantidad inicial de flechas:\n"))
arco = Flechas(cantidad_inicial)

while True:
    limpiar_consola()

    print("1. Mostrar cantidad de flechas disponibles")
    print("2. Cargar flechas")
    print("3. Disparar flecha")
    print("0. Salir")

    opcion = input("Elige una opcion:")

    if opcion == "1":
        arco.mostrar_flechas_disponibles()
    elif opcion == "2":
        cantidad_a_cargar = int(input("Ingresa la cantidad de flechas a cargar:\n"))
        arco.cargar_flechas(cantidad_a_cargar)
    elif opcion == "3":
        arco.disparar_flecha()
    elif opcion == "0":
        print("Hasta luego")
        break
    else:
        print("Opción no válida.")

    input("Presiona enter para continuar...")
