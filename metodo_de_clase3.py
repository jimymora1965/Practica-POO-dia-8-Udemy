class Pajaro:
    alas = True

    def __init__(self, nombre, raza):
        self.n = nombre
        self.r = raza

    @classmethod
    def tipo_ave(cls):
        print(f"Las aves tienen alas: {cls.alas}")

    def cuantos_huevos(self):
        if self.r == "Canario":
            return 3  # Puedes ajustar este valor según la especie de pájaro
        else:
            return "Desconocido"

# Crear una instancia de la clase Pajaro
clara = Pajaro(nombre="Clara", raza="Canario")

# Acceder a los atributos de la instancia clara
print(f"Nombre: {clara.n}")
print(f"Raza: {clara.r}")

# Llamar al método cuantos_huevos de la instancia clara
print(f"{clara.n} pone {clara.cuantos_huevos()} huevos.")

# Acceder al método tipo_ave de la clase Pajaro
Pajaro.tipo_ave()
