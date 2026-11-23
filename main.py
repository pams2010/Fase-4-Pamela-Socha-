
from modelos.cliente import Cliente
from modelos.servicio import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from modelos.reserva import Reserva
from modelos.sistema import SistemaGestion
from excepciones.errores import (
    DatosInvalidos,
    ClienteNoEncontrado
)

import logging
import os

# CONFIGURACION DE LOGS
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# CREAR SISTEMA
sistema = SistemaGestion()

print("====================================")
print("       SOFTWARE FJ")
print(" SISTEMA DE GESTION INTEGRAL")
print("====================================")


# OPERACION 1: REGISTRO DE CLIENTE
print("\n===== OPERACION 1: CLIENTE =====")

cliente1 = Cliente(
    "123456",
    "Maria Perez",
    "3001234567",
    "maria@gmail.com"
)

try:
    sistema.registrar_cliente(cliente1)
    print("Cliente registrado correctamente.")

except Exception as error:
    print("Error:", error)
    logging.error("Error registrando cliente: %s", error)


# OPERACION 2: SEGUNDO CLIENTE
print("\n===== OPERACION 2: SEGUNDO CLIENTE =====")

cliente2 = Cliente(
    "654321",
    "Carlos Gomez",
    "3109876543",
    "carlos@gmail.com"
)

try:
    sistema.registrar_cliente(cliente2)
    print("Segundo cliente registrado.")

except Exception as error:
    print("Error:", error)
    logging.error("Error registrando segundo cliente: %s", error)


# OPERACION 3: CLIENTE INVALIDO
print("\n===== OPERACION 3: CLIENTE INVALIDO =====")

cliente_invalido = Cliente(
    "",
    "Ana",
    "3000000000",
    "correo_invalido"
)

try:
    sistema.registrar_cliente(cliente_invalido)

except Exception as error:
    print("Error controlado:", error)
    logging.error("Cliente invalido: %s", error)


# OPERACION 4: REGISTRO DE SALA
print("\n===== OPERACION 4: RESERVA DE SALA =====")

servicio1 = ReservaSala(
    "S001",
    "Reserva de sala",
    50000
)

try:
    sistema.registrar_servicio(servicio1)
    print(servicio1.mostrar_detalles())

except Exception as error:
    print("Error:", error)
    logging.error("Error de servicio: %s", error)


# OPERACION 5: ALQUILER DE EQUIPOS
print("\n===== OPERACION 5: ALQUILER DE EQUIPOS =====")

servicio2 = AlquilerEquipos(
    "S002",
    "Alquiler de computadores",
    80000,
    10000
)

try:
    sistema.registrar_servicio(servicio2)
    print(servicio2.mostrar_detalles())

except Exception as error:
    print("Error:", error)
    logging.error("Error de servicio: %s", error)


# OPERACION 6: ASESORIA
print("\n===== OPERACION 6: ASESORIA =====")

servicio3 = AsesoriaEspecializada(
    "S003",
    "Asesoria en software",
    100000,
    20000
)

try:
    sistema.registrar_servicio(servicio3)
    print(servicio3.mostrar_detalles())

except Exception as error:
    print("Error:", error)
    logging.error("Error de servicio: %s", error)


# OPERACION 7: SERVICIO INVALIDO
print("\n===== OPERACION 7: SERVICIO INVALIDO =====")

try:
    servicio_invalido = ReservaSala(
        "S004",
        "Sala invalida",
        -5000
    )
    sistema.registrar_servicio(servicio_invalido)

except Exception as error:
    print("Error controlado:", error)
    logging.error("Servicio invalido: %s", error)


# OPERACION 8: RESERVA EXITOSA
print("\n===== OPERACION 8: RESERVA EXITOSA =====")

try:
    reserva1 = Reserva(
        "R001",
        cliente1,
        servicio1,
        2
    )

    sistema.registrar_reserva(reserva1)
    reserva1.confirmar()

    print(reserva1.mostrar_reserva())
    print("Reserva confirmada correctamente.")

except Exception as error:
    print("Error:", error)
    logging.error("Error en reserva: %s", error)


# OPERACION 9: RESERVA INCORRECTA
print("\n===== OPERACION 9: RESERVA INCORRECTA =====")

try:
    reserva_invalida = Reserva(
        "R002",
        cliente1,
        servicio2,
        0
    )

    sistema.registrar_reserva(reserva_invalida)

except Exception as error:
    print("Error controlado:", error)
    logging.error("Reserva incorrecta: %s", error)


# OPERACION 10: EXCEPCIONES PERSONALIZADAS
print("\n===== OPERACION 10: EXCEPCIONES =====")

try:
    raise DatosInvalidos("Prueba de error controlado.")

except DatosInvalidos as error:
    print("Excepcion personalizada:", error)
    logging.error("Excepcion personalizada: %s", error)

finally:
    print("Finalizo la prueba de excepciones.")
    logging.info("Finalizo la prueba de excepciones.")


# OPERACION 11: BLOQUE ELSE

# OPERACION 16: CALCULOS CON IMPUESTOS Y DESCUENTOS

print("\n===== OPERACION 16: CALCULOS =====")

try:
    print(
        "Costo normal:",
        servicio1.calcular_costo(2)
    )

    print(
        "Costo con impuesto:",
        servicio1.calcular_costo(2, 0.19)
    )

    print(
        "Costo con impuesto y descuento:",
        servicio1.calcular_costo(2, 0.19, 10000)
    )

    print(
        "Calculo alternativo:",
        servicio1.calcular_con_impuestos(2)
    )

except Exception as error:
    print("Error en los calculos:", error)
    logging.error("Error en los calculos: %s", error)

print("\n===== OPERACION 11: PRUEBA ELSE =====")

try:
    total = reserva1.calcular_total()
    print("Calculo realizado correctamente.")

except Exception as error:
    print("Error en el calculo:", error)
    logging.error("Error calculando reserva: %s", error)

else:
    print("El total de la reserva es: $", total)
    logging.info("Calculo realizado correctamente.")


# OPERACION 12: PROCESAR RESERVA
print("\n===== OPERACION 12: PROCESAR RESERVA =====")

try:
    reserva1.procesar()
    print("Reserva procesada correctamente.")
    print("Estado actual:", reserva1.estado)

except Exception as error:
    print("Error procesando reserva:", error)
    logging.error("Error procesando reserva: %s", error)


# OPERACION 13: CANCELAR RESERVA
print("\n===== OPERACION 13: CANCELAR RESERVA =====")

try:
    reserva2 = Reserva(
        "R003",
        cliente2,
        servicio2,
        1
    )

    sistema.registrar_reserva(reserva2)
    reserva2.cancelar()

    print("Reserva cancelada correctamente.")
    print("Estado actual:", reserva2.estado)

except Exception as error:
    print("Error cancelando reserva:", error)
    logging.error("Error cancelando reserva: %s", error)


# OPERACION 14: BUSCAR CLIENTE INEXISTENTE
print("\n===== OPERACION 14: BUSQUEDA DE CLIENTE =====")

try:
    sistema.buscar_cliente("999999")

except ClienteNoEncontrado as error:
    print("Excepcion personalizada:", error)

    if error.__cause__ is not None:
        print("Error original:", error.__cause__)

    logging.error("Busqueda fallida: %s", error)


# OPERACION 15: CONSULTA DE RESERVA
print("\n===== OPERACION 15: CONSULTA DE RESERVA =====")

try:
    reserva_consultada = sistema.buscar_reserva("R001")
    print(reserva_consultada.mostrar_reserva())

except Exception as error:
    print("Error consultando reserva:", error)
    logging.error("Error consultando reserva: %s", error)


# RESUMEN GENERAL
print("\n===== RESUMEN DEL SISTEMA =====")

print("Total de clientes:", sistema.cantidad_clientes())
print("Total de servicios:", sistema.cantidad_servicios())
print("Total de reservas:", sistema.cantidad_reservas())

print("\n===== SISTEMA FINALIZADO =====")

logging.info("Sistema Software FJ finalizado.")
