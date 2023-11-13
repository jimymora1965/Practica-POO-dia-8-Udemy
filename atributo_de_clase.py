class Personaje:
    # Atributo de clase
    real = False

    def __init__(self, especie, magico, edad):
        # Atributos de instancia
        self.especie = especie
        self.magico = magico
        self.edad = edad

# Crear una instancia de la clase Personaje
harry_potter = Personaje(especie="Humano", magico=True, edad=17)

# Acceder a los atributos de la instancia
print(f"Especie: {harry_potter.especie}")
print(f"Es mágico: {harry_potter.magico}")
print(f"Edad: {harry_potter.edad}")
print(f"Real: {Personaje.real}")  # Acceder al atributo de clase
