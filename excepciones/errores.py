
class ErrorSistema(Exception):
    """Excepcion base del sistema Software FJ."""
    pass


class ClienteNoEncontrado(ErrorSistema):
    """Error cuando un cliente no existe."""
    pass


class ServicioNoEncontrado(ErrorSistema):
    """Error cuando un servicio no existe."""
    pass


class ReservaNoEncontrada(ErrorSistema):
    """Error cuando una reserva no existe."""
    pass


class DatosInvalidos(ErrorSistema):
    """Error cuando los datos ingresados son incorrectos."""
    pass


class ServicioNoDisponible(ErrorSistema):
    """Error cuando un servicio no esta disponible."""
    pass


class ReservaInvalida(ErrorSistema):
    """Error cuando una reserva no cumple las condiciones."""
    pass


class OperacionNoPermitida(ErrorSistema):
    """Error cuando se intenta realizar una operacion prohibida."""
    pass


class CalculoInconsistente(ErrorSistema):
    """Error cuando un calculo produce un resultado incorrecto."""
    pass


class ParametroFaltante(ErrorSistema):
    """Error cuando falta un parametro obligatorio."""
    pass
