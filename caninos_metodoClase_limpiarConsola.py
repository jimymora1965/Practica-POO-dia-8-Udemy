import os
class Caninos():

    nobles = "Amorosos"
    ascendencia = "Lobo"

    def __init__(self, raza, origen, nombre):
        self.r = raza
        self.o = origen
        self.n = nombre

    
    @classmethod
    def caracter(cls):
        print(f"Todos los perros independiente de la raza son {cls.nobles}")

    @classmethod
    def historia(cls):
        print(f"Todos los perros descienden del {cls.ascendencia}")


def limpiar_consola():
    if os.name == "nt":
        os.system("cls")

limpiar_consola()
oddie = Caninos(raza="chihuahua", origen= "mexico", nombre= "Oddie Mora")
print(f"Mi perro es de raza {oddie.r}")
Caninos.caracter()
Caninos.historia()