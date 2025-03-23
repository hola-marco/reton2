from   historial import HistorialServicio
class HistorialMascota(HistorialServicio):
    def __init__(self):
        self.servicios = []

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)

    def mostrar_historial(self):
        if not self.servicios:
            print("No hay servicios registrados.")
        else:
            for servicio in self.servicios:
                print(f" - {servicio}")
