
from modelos.entidad import Entidad


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, telefono, correo):
        super().__init__(identificacion, nombre)

        self._telefono = telefono
        self._correo = correo

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def telefono(self):
        return self._telefono

    @property
    def correo(self):
        return self._correo

    def mostrar_informacion(self):
        return (
            f"Identificación: {self._identificacion}\n"
            f"Nombre: {self._nombre}\n"
            f"Teléfono: {self._telefono}\n"
            f"Correo: {self._correo}"
        )

    def validar_datos(self):

        if not self._identificacion or not self._nombre:
            raise ValueError(
                "La identificación y el nombre son obligatorios."
            )

        if not self._telefono or not self._telefono.isdigit():
            raise ValueError("El teléfono debe contener solo números.")

        if not self._correo or "@" not in self._correo:
            raise ValueError("El correo electrónico no es válido.")

        return True

