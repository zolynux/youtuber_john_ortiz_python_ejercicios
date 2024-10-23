# Ejercicio 39: Calcular el valor futuro para una cantidad, interés y números de años específicos.


def valor_futuro(vp, i, n):
    """
    Calcular el valor futuro.
    """
    return vp * (1 + i) ** n


valor_presente = 10000
interes = 3.5
periodo = 7

print(valor_futuro(valor_presente, interes, periodo))
