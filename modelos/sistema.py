
import logging

from excepciones.errores import (
    ClienteNoEncontrado,
    ServicioNoEncontrado,
    ReservaNoEncontrada,
    DatosInvalidos
)


class SistemaGestion:

    def __init__(self):
        # LISTAS INTERNAS DEL SISTEMA
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

    # REGISTRAR CLIENTES
    def registrar_cliente(self, cliente):

        cliente.validar_datos()

        for existente in self.__clientes:
            if existente.identificacion == cliente.identificacion:
                raise DatosInvalidos(
                    "El cliente ya se encuentra registrado."
                )

        self.__clientes.append(cliente)
        logging.info("Cliente registrado correctamente.")

    # REGISTRAR SERVICIOS
    def registrar_servicio(self, servicio):

        for existente in self.__servicios:
            if existente.codigo == servicio.codigo:
                raise DatosInvalidos(
                    "El servicio ya se encuentra registrado."
                )

        self.__servicios.append(servicio)
        logging.info("Servicio registrado correctamente.")

    # REGISTRAR RESERVAS
    def registrar_reserva(self, reserva):

        for existente in self.__reservas:
            if existente.codigo == reserva.codigo:
                raise DatosInvalidos(
                    "La reserva ya se encuentra registrada."
                )

        if reserva.cliente not in self.__clientes:
            raise ClienteNoEncontrado(
                "El cliente no esta registrado en el sistema."
            )

        if reserva.servicio not in self.__servicios:
            raise ServicioNoEncontrado(
                "El servicio no esta registrado en el sistema."
            )

        self.__reservas.append(reserva)
        logging.info("Reserva registrada correctamente.")

    # BUSCAR CLIENTE
    def buscar_cliente(self, identificacion):

        try:
            for cliente in self.__clientes:
                if cliente.identificacion == identificacion:
                    return cliente

            raise LookupError("Cliente no encontrado.")

        except LookupError as error:
            logging.error("Error buscando cliente: %s", error)

            raise ClienteNoEncontrado(
                "No existe un cliente con esa identificacion."
            ) from error

    # BUSCAR SERVICIO
    def buscar_servicio(self, codigo):

        try:
            for servicio in self.__servicios:
                if servicio.codigo == codigo:
                    return servicio

            raise LookupError("Servicio no encontrado.")

        except LookupError as error:
            logging.error("Error buscando servicio: %s", error)

            raise ServicioNoEncontrado(
                "No existe un servicio con ese codigo."
            ) from error

    # BUSCAR RESERVA
    def buscar_reserva(self, codigo):

        try:
            for reserva in self.__reservas:
                if reserva.codigo == codigo:
                    return reserva

            raise LookupError("Reserva no encontrada.")

        except LookupError as error:
            logging.error("Error buscando reserva: %s", error)

            raise ReservaNoEncontrada(
                "No existe una reserva con ese codigo."
            ) from error

    # CONSULTAR INFORMACION
    def mostrar_clientes(self):
        return [
            cliente.mostrar_informacion()
            for cliente in self.__clientes
        ]

    def mostrar_servicios(self):
        return [
            servicio.mostrar_detalles()
            for servicio in self.__servicios
        ]

    def mostrar_reservas(self):
        return [
            reserva.mostrar_reserva()
            for reserva in self.__reservas
        ]

    # CONSULTAR CANTIDADES
    def cantidad_clientes(self):
        return len(self.__clientes)

    def cantidad_servicios(self):
        return len(self.__servicios)

    def cantidad_reservas(self):
        return len(self.__reservas)
