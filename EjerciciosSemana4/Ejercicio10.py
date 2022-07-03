#Conversion de la edad de perros a años humanos

#ln logaritmo neperiano

import math
def edad_perro_a_humano(edad):
    edad = float(edad)
    try:
        if edad > 0:
            años_humanos = 16 * (math.log(edad)) + 31
            return round(años_humanos, 4)
    except ValueError:
        print('Ingrese un numero mayor a 0')
        

print(edad_perro_a_humano(-1))
    