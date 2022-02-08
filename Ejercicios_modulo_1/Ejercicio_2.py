from asyncore import read
a = float(input('cual es el valor de a?')) #pide al usuario introducir un numero, escribiendo a terminal y convirtiendo el valor a float
b = float(input('cual es el valor de b?')) #pide al usuario introducir un numero, escribiendo a terminal y convirtiendo el valor a float
sum = a + b #realiza la suma
print('la suma es ' + str(sum)) #trasnformamos de float a string

#################################################################################

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

################################################################################

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
fecha = str(date.today()) #converti del formato fecha al fortmato string

# Mostramos la fecha en la consola
print('hoy es ' + fecha)

