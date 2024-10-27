# Ejercicio 67: Convertir  kilospascales (kPa) en presión, psi, mmHg y atm.


def conversion_kilospascales(kpa):
    psi = kpa / 6.89475729
    mmhg = kpa * 760 / 101.325
    atm = kpa / 101.325

    return psi, mmhg, atm


kilospascales = float(input("Escriba la presión en Kilospascales (kPa): "))

print(conversion_kilospascales(kilospascales))
