#Ejercicio12. Calcular energia cinetica

from fractions import Fraction

masa = float(input('Ingrese la masa kg: '))
velocidad = float(input('Ingrese la velocidad m/s: '))
formula =  (Fraction(1,2) * masa) * velocidad**2
formula = round(formula, 2)
print('La energia cinetica es igual a: {} julios'.format(formula))