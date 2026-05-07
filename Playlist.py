class Playlist:
    def __init__(self, nombre, canciones):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    
    def reproductir(self):
        print(f"Reproduciendo playlist: {self.nombre}")
        for cancion in self.canciones:
            print(f"Reproduciendo: {cancion}")
    
    def ver_canciones(self):
        print(f"Canciones en la playlist '{self.nombre}':")
        for cancion in self.canciones:
            print(cancion)

# Ejemplo de uso
playlist = Playlist("Mi Playlist Favorita", [])
playlist.agregar_cancion("Bohemian Rhapsody")
playlist.agregar_cancion("Starme up")
playlist.ver_canciones()

playlist.reproductir()