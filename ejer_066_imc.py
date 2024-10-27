# Ejercicio 66: Calcular el índice de masa corporal (IMC).


def imc(estatura, peso):
    """
    Calcular el índice de masa corporal
    """
    return peso / estatura**2


peso = float(input("Escriba su peso (kg): "))
estatura = float(input("Escriba su estatura (m): "))

indice = imc(estatura, peso)

print("Su IMC es: {}".format(indice))
