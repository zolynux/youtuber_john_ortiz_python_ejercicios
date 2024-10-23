# Ejercicio 38: Resolver la expresión algebraica (x + y) * (x + y)

# (x + y) * (x + y) = x^2 + 2xy + y^2


def evaluar_exresion(x, y):
    """
    Resuelve la expresión algebraica (x + y) * (x + y)
    """
    return x**2 + 2 * x * y + y**2


x = float(input("Esciba el valor de x: "))
y = float(input("Esciba el valor de y: "))

print(evaluar_exresion(x, y))
