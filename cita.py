from datetime import datetime
class Cita:
    def __init__(self, cliente, mascota, fecha, servicio):
        self.cliente = cliente
        self.mascota = mascota
        self.fecha = fecha
        self.servicio = servicio

    def __str__(self):
        return f"Cita: {self.fecha}, Cliente: {self.cliente.nombre}, Mascota: {self.mascota.nombre}, Servicio: {self.servicio}"
    from datetime import datetime
def validar_fecha(func):
    def wrapper(*args, **kwargs):
        fecha = args[2]
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
            return func(*args, **kwargs)
        except ValueError:
            print("Error: Formato de fecha incorrecto. Use YYYY-MM-DD.")
    return wrapper
class CitaFactory:
    @staticmethod
    @validar_fecha
    def crear_cita(cliente, mascota, fecha, servicio):
        return Cita(cliente, mascota, fecha, servicio)
