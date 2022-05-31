#Ejercicio3 Calcular la altura maxima (Ymax) y la distancia 
# maxima (Xmax) de un proyectil

from cmath import sin
import math


def proyectil (a, Vo): #Parametro: Angulo de inclinacion (a) y velocidad inicial (Vo)
    radianes = a * (math.pi/180) #Conversion de los angulos a radianes
    a = radianes
    Xmax = ((Vo**2)* math.sin(a) * ( 2 * a)) / 9.86 #Formula distancia maxima
    Ymax = ((Vo**2) * math.sin(a) ** 2 * (a)) / 2*9.86 #Formula altura maxima
    return Xmax, Ymax

print(proyectil(0, 0)) #Prueba
    