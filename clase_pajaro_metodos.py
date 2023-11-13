class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.c = color
        self.e = especie
    
    def piar(self):
        print("pio")

    def volar(self):
        print("El pajaro ha volado {metros} metros")

piolin = Pajaro("amarillo", "canario")
print(piolin)