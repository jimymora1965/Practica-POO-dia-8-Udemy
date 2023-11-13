class Mi_clase:
    variable_de_clase = "Mi variable"

    @classmethod
    def metodo_clase(cls):
        print(f"Esta es mi {cls.variable_de_clase}")

Mi_clase.metodo_clase()