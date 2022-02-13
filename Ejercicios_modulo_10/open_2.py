try:
    open(".\Ejercicios_modulo_10\mars.jpg")
except FileNotFoundError as err: #considera al error como error convirtiendolo en un valor
    print("got a problem trying to read the file:", err) #basicamente nos da la informacion directa del error y todo, pero de una manera mas simplificada y consisa