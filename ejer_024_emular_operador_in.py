# Ejercicio 24: Simular el funcionamiento del operador in.

print(5 in [2,3,5,7, 11])
print('k' in 'Fork')
print('i' in 'Fork')

print('=' * 20)


def pertenece_a(lista, elemento):
    # Comprueba si un elemento está disponible en una lista.
    for e in lista:
        if elemento == e:
            return True
    return False


print(pertenece_a([2,3,5,7, 11], 5))
print(pertenece_a([2,3,5,7, 11], 18))
print(pertenece_a('Fork', 'k'))
print(pertenece_a('Fork', 'i'))

print('=' * 20)

print(pertenece_a(['F','o','r','k'], 'k'))
print(pertenece_a(['F','o','r','k'], 'i'))

