
# Clase para gestionar clientes

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def __str__(self):
        return f"Cliente: {self.nombre}, Teléfono: {self.telefono}"
