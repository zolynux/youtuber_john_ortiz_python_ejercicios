# Ejercicio 9: Mostrar la fecha de un evento almacenada en una tabla.

# Se define una tupla que almacena la fecha del evento (año, mes, día)
fecha_evento = (2023, 9, 14)

# Imprime el tipo de dato de la variable fecha_evento (que es una tupla)
print(type(fecha_evento))

# Imprime la tupla que contiene la fecha del evento
print(fecha_evento)

# Imprime un mensaje con la fecha del evento en formato de tupla
print("El evento programado será para la fecha:", fecha_evento)

# Utiliza el operador % para formatear e imprimir la fecha del evento en un formato específico
print("El evento programado será para la fecha: %i/%i/%i" % fecha_evento)

# Desempaqueta la tupla en variables para el año, mes y día
agnio, mes, dia = fecha_evento  # agnio = año

# Imprime la fecha del evento utilizando el método format para darle un formato específico
print("El evento programado será para la fecha: {}/{}/{}".format(agnio, mes, dia))
