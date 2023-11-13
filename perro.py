class Caninos:
    def __init__(self, nombre, raza, edad):
        self.n = nombre
        self.r = raza
        self.e = edad

blanco = Caninos(nombre = "Oddie", raza ="Chihuahua", edad = "5 años")
cafe = Caninos(nombre = "Mocca", raza = "Chihuahua", edad = "4 años" )

print(blanco.n, blanco.r, blanco.e)