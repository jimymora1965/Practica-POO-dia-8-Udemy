""" Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False. """

class Jugador:
    vivo = False

    def __init__(self, nombre):
        self.nombre = nombre

    def info(self):
        print(f"{self.nombre} {'está' if Jugador.vivo else 'no está'} vivo.")

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print("¡Reviviendo al jugador!")

# Crear instancias de la clase Jugador
jugador1 = Jugador(nombre="Juan")
jugador2 = Jugador(nombre="Maria")

# Información inicial
jugador1.info()  # Juan no está vivo.
jugador2.info()  # Maria no está vivo.

# Llamar al método de clase revivir
Jugador.revivir()

# Información después de revivir
jugador1.info()  # Juan está vivo.
jugador2.info()  # Maria está vivo.
