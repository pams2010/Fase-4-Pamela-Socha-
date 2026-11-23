
from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio_base):

        if not codigo or not nombre:
            raise ValueError(
                "El codigo y el nombre son obligatorios."
            )

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._codigo = codigo
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    # APLICAR IMPUESTOS Y DESCUENTOS
    def _aplicar_ajustes(self, subtotal, impuesto, descuento):

        if not 0 <= impuesto <= 1:
            raise ValueError(
                "El impuesto debe estar entre 0 y 1."
            )

        if descuento < 0:
            raise ValueError(
                "El descuento no puede ser negativo."
            )

        if descuento > subtotal:
            raise ValueError(
                "El descuento no puede superar el subtotal."
            )

        total = subtotal - descuento

        return total * (1 + impuesto)

    # METODO ABSTRACTO CON PARAMETROS OPCIONALES
    @abstractmethod
    def calcular_costo(
        self,
        cantidad=1,
        impuesto=0,
        descuento=0
    ):
        pass

    @abstractmethod
    def mostrar_detalles(self):
        pass

    # CALCULO ALTERNATIVO CON IMPUESTOS
    def calcular_con_impuestos(
        self,
        cantidad=1,
        impuesto=0.19,
        descuento=0
    ):

        return self.calcular_costo(
            cantidad,
            impuesto,
            descuento
        )


# SERVICIO 1: RESERVA DE SALAS
class ReservaSala(Servicio):

    def calcular_costo(
        self,
        cantidad=1,
        impuesto=0,
        descuento=0
    ):

        if cantidad <= 0:
            raise ValueError(
                "La cantidad de horas debe ser positiva."
            )

        subtotal = self._precio_base * cantidad

        return self._aplicar_ajustes(
            subtotal,
            impuesto,
            descuento
        )

    def mostrar_detalles(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Precio por hora: ${self._precio_base}\n"
            f"Tipo: Reserva de salas"
        )


# SERVICIO 2: ALQUILER DE EQUIPOS
class AlquilerEquipos(Servicio):

    def __init__(self, codigo, nombre, precio_base, mantenimiento):

        super().__init__(codigo, nombre, precio_base)

        if mantenimiento < 0:
            raise ValueError(
                "El mantenimiento no puede ser negativo."
            )

        self._mantenimiento = mantenimiento

    def calcular_costo(
        self,
        cantidad=1,
        impuesto=0,
        descuento=0
    ):

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser positiva."
            )

        subtotal = (
            self._precio_base + self._mantenimiento
        ) * cantidad

        return self._aplicar_ajustes(
            subtotal,
            impuesto,
            descuento
        )

    def mostrar_detalles(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Precio base: ${self._precio_base}\n"
            f"Mantenimiento: ${self._mantenimiento}\n"
            f"Tipo: Alquiler de equipos"
        )


# SERVICIO 3: ASESORIAS ESPECIALIZADAS
class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio_base, recargo):

        super().__init__(codigo, nombre, precio_base)

        if recargo < 0:
            raise ValueError(
                "El recargo no puede ser negativo."
            )

        self._recargo = recargo

    def calcular_costo(
        self,
        cantidad=1,
        impuesto=0,
        descuento=0
    ):

        if cantidad <= 0:
            raise ValueError(
                "La cantidad de asesorias debe ser positiva."
            )

        subtotal = (
            self._precio_base + self._recargo
        ) * cantidad

        return self._aplicar_ajustes(
            subtotal,
            impuesto,
            descuento
        )

    def mostrar_detalles(self):

        return (
            f"Servicio: {self._nombre}\n"
            f"Precio base: ${self._precio_base}\n"
            f"Recargo: ${self._recargo}\n"
            f"Tipo: Asesoria especializada"
        )
