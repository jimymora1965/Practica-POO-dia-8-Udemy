class Dinosaurio:
    def __init__(self, nombre, especie, dieta):
        self.nombre = nombre
        self.especie = especie
        self.dieta = dieta

# Crear instancias de la clase Dinosaurio
velociraptor = Dinosaurio(nombre="Velociraptor", especie="Velociraptor mongoliensis", dieta="Carnívoro")
tiranosaurio_rex = Dinosaurio(nombre="Tiranosaurio Rex", especie="Tyrannosaurus rex", dieta="Carnívoro")
braquiosaurio = Dinosaurio(nombre="Braquiosaurio", especie="Brachiosaurus", dieta="Herbívoro")

# Acceder a los atributos de las instancias
print(f"Nombre: {velociraptor.nombre}, Especie: {velociraptor.especie}, Dieta: {velociraptor.dieta}")
print(f"Nombre: {tiranosaurio_rex.nombre}, Especie: {tiranosaurio_rex.especie}, Dieta: {tiranosaurio_rex.dieta}")
print(f"Nombre: {braquiosaurio.nombre}, Especie: {braquiosaurio.especie}, Dieta: {braquiosaurio.dieta}")
