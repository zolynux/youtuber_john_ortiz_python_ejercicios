# Ejericio 56: Obtener el tamaño de la ventana del terminal

import fcntl, termios, struct


def calcular_tamagnio_terminal():
    th, tw, hp, wp = struct.unpack(
        "HHHH", fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack("HHHH", 0, 0, 0, 0))
    )

    return tw, th


print(calcular_tamagnio_terminal())
