# Ejercicio 45: Ejercutar un comando externo por medio de la función call.

from subprocess import call

print(call(["ping", "google.com"]))
