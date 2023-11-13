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
        if self.t =="Canario":
            return "3"
        else:
            return "Desconocido"
def clear_pantalla():
    if os.name == "nt":
        os.system("cls")

clear_pantalla()   
piolin = Pajaro(tipo = "Canario", color= "Amarillo")
piolin.volar()
print(f"El {piolin.t} pone {piolin.cantidad_huevos()} huevos")

