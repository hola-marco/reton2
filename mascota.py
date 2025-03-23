from historialMascota import HistorialMascota
class Mascota:
    def __init__(self, nombre, especie, raza):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.historial = HistorialMascota()

    def __str__(self):
        return f"Mascota: {self.nombre}, Especie: {self.especie}, Raza: {self.raza}"