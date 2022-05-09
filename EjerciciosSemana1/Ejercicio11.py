#Ejercicio11. Convertir pies y pulgadas a centimetros

pies = float(input('Ingrese los pies -ft-: '))
pulgadas = float(input('Ingrese las pulgadas -in-: '))
cms = ((pies / 12) + pulgadas) * 2.54
cms = round(cms, 2)
print('Eso es igual a: {} cms'.format(cms))