class PlataformaStreaming:
    def __init__(self, nombre, genero):
        self. n = nombre
        self. g = genero
        
netflix = PlataformaStreaming(nombre = "Superman", genero = "Accion")
hbo_max = PlataformaStreaming(nombre = "Porky", genero = "Cricaturas")
amazon_prime_video = PlataformaStreaming(nombre = "Wick", genero = "Accion")

print(f"Nombre: {netflix.n}, Genero: {netflix.g}")
print(f"Nombre: {hbo_max.n}, Genero: {hbo_max.g}")
print(f"Nombre: {amazon_prime_video.n}, Genero: {amazon_prime_video.g}")