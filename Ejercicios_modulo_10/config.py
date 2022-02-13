def main():
    try:
        configuration = open('.\Ejercicios_modulo_10\config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!") #pese a que el archivo si existe, no lo abre y dice que no se encontro el archivo, cosa que no es cierto
    except PermissionError:
        print("Found config.txt but it is a directory, couldn't read it") #agregando esta linea, ahora si detecta el error real
    except (BlockingIOError, TimeoutError): #se puedene agrupar errores para mostrar solo un mensaje por medio de parentesis, pero solo se recomienda si no se deben tratar por separado
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()