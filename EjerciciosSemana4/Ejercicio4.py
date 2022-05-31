#Ejercicio4 Calculo del area de un triangulo

import math


def area_triangulo (a, b, c): #Parametros: lados del triangulo
    s = (a + b + c) / 2 #semiperimetro
    area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #Calculo area del triangulo
    return area

print(area_triangulo(0, 0, 0))