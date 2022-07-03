# Definir una función para calcular el seno de x empleando la Serie Taylor, los
# datos de entrada de la función son el ángulo el cual se debe convertir a
# radianes y la cantidad de veces a iterar la función

import math


def cal_seno(ang=int, nterm=int):
    ang = math.radians(ang)
    sen_x = 0.0
    for k in range(nterm+1):
        sen_x = sen_x + (-1)**k * ang**(2*k*1) / math.factorial((2*k+1))
    return sen_x

print(cal_seno(180, 5))

