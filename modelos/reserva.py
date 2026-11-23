
from datetime import datetime

from excepciones.errores import (
    DatosInvalidos,
    ReservaInvalida,
    OperacionNoPermitida
)


class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):

        if not codigo:
            raise DatosInvalidos("El codigo de la reserva es obligatorio.")

        if cliente is None or servicio is None:
            raise DatosInvalidos(
                "La reserva debe tener un cliente y un servicio."
            )

        try:
            duracion = float(duracion)

            if duracion <= 0:
                raise ValueError("La duracion debe ser mayor que cero.")

        except (TypeError, ValueError) as error:
            raise DatosInvalidos(
                "La duracion ingresada no es valida."
            ) from error

        self._codigo = codigo
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._fecha = datetime.now()

    @property
    def codigo(self):
        return self._codigo

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def estado(self):
        return self._estado

    @property
    def duracion(self):
        return self._duracion

    def cambiar_estado(self, nuevo_estado):

        estados_validos = [
            "Pendiente",
            "Confirmada",
            "Cancelada",
            "Finalizada"
        ]

        if nuevo_estado not in estados_validos:
            raise ReservaInvalida("Estado de reserva no valido.")

        self._estado = nuevo_estado

    def confirmar(self):

        if self._estado != "Pendiente":
            raise OperacionNoPermitida(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "Confirmada"

    def cancelar(self):

        if self._estado not in ["Pendiente", "Confirmada"]:
            raise OperacionNoPermitida(
                "No se puede cancelar esta reserva."
            )

        self._estado = "Cancelada"

    def procesar(self):

        if self._estado != "Confirmada":
            raise OperacionNoPermitida(
                "La reserva debe estar confirmada para procesarse."
            )

        self._estado = "Finalizada"

    def calcular_total(self):

        try:
            return self._servicio.calcular_costo(self._duracion)

        except (ValueError, TypeError) as error:
            raise ReservaInvalida(
                "No fue posible calcular el costo de la reserva."
            ) from error

    def mostrar_reserva(self):

        return (
            f"\n===== INFORMACION DE LA RESERVA =====\n"
            f"Codigo: {self._codigo}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duracion: {self._duracion}\n"
            f"Estado: {self._estado}\n"
            f"Fecha: {self._fecha.strftime('%d/%m/%Y %H:%M')}\n"
            f"Total: ${self.calcular_total()}"
        )
