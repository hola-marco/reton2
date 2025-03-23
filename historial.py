from abc import ABC,abstractmethod
class HistorialServicio(ABC):
    @abstractmethod
    def agregar_servicio(self, servicio):
        pass

    @abstractmethod
    def mostrar_historial(self):
        pass