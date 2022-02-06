#programa que pasa de parsec a años luz o viceversa
from telnetlib import theNULL

a = int(input('si desea convertir de parsec a años luz presione 1, si quiere convertir de años luz a parsec 2, de lo contrario presione cualquier otro numero' ))
if a == 1:
    x = float(input('cual es la cantidad de parsec que desea convertir?'))
    b = str(x*3.26156)
    print(str(x) + ' parsec son ' + b + ' años luz')
elif a == 2:
    x = float(input('cual es la cantidad de años luz que desea convertir?'))
    b = str(x/3.26156)
    print(str(x) + ' años luz son ' + b + ' parsec')
print("Gracias por utilizar el programa")