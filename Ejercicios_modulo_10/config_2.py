try:
    open(".\Ejercicios_modulo_10\config.txt")
except OSError as err:
    if err.errno == 2: #es basicamente otra manera de detectar el error, pero utilizando el numero de error "Errno", en este caso el "Errno 2"
        print("Couldn't find the config.txt file!")
    elif err.errno == 13: #es basicamente otra manera de detectar el error, pero utilizando el numero de error "Errno", en este otro caso el "Errno 13"
        print("Found config.txt but couldn't read it")