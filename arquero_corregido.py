import os

class ArcoFlechas:
    def __init__(self, cantidad_inicial):
        self.cantidad_flechas = cantidad_inicial

    def cargar_flechas(self):
        cantidad = int(input("Ingresa la cantidad de flechas que deseas cargar: "))
        self.cantidad_flechas += cantidad
        print(f"Has cargado {cantidad} flechas. Ahora tienes {self.cantidad_flechas} flechas.")

    def disparar_flecha(self):
        if self.cantidad_flechas > 0:
            self.cantidad_flechas -= 1
            print("¡Flecha lanzada!")
        else:
            print("¡No tienes flechas! Carga flechas antes de disparar.")

    def mostrar_flechas_disponibles(self):
        print(f"Tienes {self.cantidad_flechas} flechas disponibles.")

def limpiar_consola():
    os.system('cls')

# Ejemplo de uso con input
cantidad_inicial = int(input("Ingresa la cantidad inicial de flechas: "))

arco = ArcoFlechas(cantidad_inicial)

while True:
    limpiar_consola()
    print("\n1. Mostrar flechas disponibles")
    print("2. Cargar flechas")
    print("3. Disparar flecha")
    print("0. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        arco.mostrar_flechas_disponibles()
    elif opcion == "2":
        arco.cargar_flechas()
    elif opcion == "3":
        arco.disparar_flecha()
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
    
    input("Presiona Enter para continuar...")
