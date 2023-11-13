class Pajaro:
    # Atributo de clase
    alas = True

    # Constructor con atributos de color y especie
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    # Método para hacer que el pájaro píe
    def piar(self):
        print("Pío, pío!")

    # Método para simular que el pájaro está volando
    def volar(self):
        print(f"{self.color} {self.especie} está volando.")

# Crear un objeto llamado piolin
piolin = Pajaro(color="amarillo", especie="canario")

# Acceder a los atributos del objeto
print(f"Color de Piolín: {piolin.color}")
print(f"Especie de Piolín: {piolin.especie}")

# Llamar a los métodos del objeto
piolin.piar()
piolin.volar()
