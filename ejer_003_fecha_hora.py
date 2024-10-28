# Ejercicio 3: Obtener la fecha y hora actuales en el sistema.

# Importa el módulo datetime que proporciona clases para manejar fechas y horas
import datetime

# Obtiene la fecha y hora actuales del sistema
ahora = datetime.datetime.now()

# Imprime la fecha y hora actuales
print(ahora)

# Imprime el tipo de dato de la variable ahora
print(type(ahora))

# Formatea la fecha y hora actuales como una cadena en el formato especificado
print(ahora.strftime("%d/%m/%y %H:%M:%S"))
