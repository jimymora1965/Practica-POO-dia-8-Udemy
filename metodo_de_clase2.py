class Tarea:
    actividad = "Mi tarea de georafia"

    @classmethod
    def colegio(cls):
        print(f"Tengo que hacer {cls.actividad} para mañana")

Tarea.colegio()