from cliente import Cliente
from mascota import Mascota
from cita import CitaFactory
import json
from os import path
class Veterinaria:
    def __init__(self):
        self.clientes = []
        self.citas = []

    def agregar_cliente(self, cliente):
        if any(c.nombre == cliente.nombre for c in self.clientes):
            print("Error: Ya existe un cliente con ese nombre.")
        else:
            self.clientes.append(cliente)
            print(f"Cliente {cliente.nombre} registrado con éxito.")

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        print("Error: Cliente no encontrado.")
        return None

    def agregar_cita(self, cita):
        self.citas.append(cita)
        print(f"Cita para {cita.mascota.nombre} registrada con éxito.")

    def cancelar_cita(self, fecha, nombre_mascota):
        cita_a_cancelar = None
        for cita in self.citas:
            if cita.fecha == fecha and cita.mascota.nombre == nombre_mascota:
                cita_a_cancelar = cita
                break
        if cita_a_cancelar:
            self.citas.remove(cita_a_cancelar)
            print(f"Cita del {fecha} para {nombre_mascota} cancelada.")
        else:
            print("Error: Cita no encontrada.")

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(cliente)
                for mascota in cliente.mascotas:
                    print(f"  {mascota}")

    def mostrar_citas(self):
        if not self.citas:
            print("No hay citas programadas.")
        else:
            for cita in self.citas:
                print(cita)

    def guardar_datos(self, archivo):
        datos = {
            "clientes": [
                {
                    "nombre": c.nombre,
                    "telefono": c.telefono,
                    "mascotas": [
                        {
                            "nombre": m.nombre,
                            "especie": m.especie,
                            "raza": m.raza,
                            "historial": m.historial.servicios
                        }
                        for m in c.mascotas
                    ]
                }
                for c in self.clientes
            ],
            "citas": [
                {
                    "cliente": c.cliente.nombre,
                    "mascota": c.mascota.nombre,
                    "fecha": c.fecha,
                    "servicio": c.servicio
                }
                for c in self.citas
            ]
        }
        with open(archivo, "w") as f:
            json.dump(datos, f, indent=4)
        print(f"Datos guardados en {archivo}.")

    def cargar_datos(self, archivo):
        if not path.exists(archivo):
            print("Error: Archivo no encontrado.")
            return
        with open(archivo, "r") as f:
            datos = json.load(f)
        for cliente_data in datos["clientes"]:
            cliente = Cliente(cliente_data["nombre"], cliente_data["telefono"])
            for mascota_data in cliente_data["mascotas"]:
                mascota = Mascota(mascota_data["nombre"], mascota_data["especie"], mascota_data["raza"])
                mascota.historial.servicios = mascota_data["historial"]
                cliente.agregar_mascota(mascota)
            self.clientes.append(cliente)
        for cita_data in datos["citas"]:
            cliente = self.buscar_cliente(cita_data["cliente"])
            if cliente:
                mascota = next((m for m in cliente.mascotas if m.nombre == cita_data["mascota"]), None)
                if mascota:
                    cita = CitaFactory.crear_cita(cliente, mascota, cita_data["fecha"], cita_data["servicio"])
                    if cita:
                        self.citas.append(cita)
        print(f"Datos cargados desde {archivo}.")