#Ejercicio15Reto Porcentajes a gastar teniendo en cuenta el salario ingresado

salario = int(input('Ingresa el salario de este mes sin comas ni puntos: '))

#Alimentos equivale al 20% del salario
alimentos = salario * 0.20
print()
print('Para alimentos destinas: ' + str(alimentos))

#Pasajes equivale al 15% del salario
pasajes = salario * 0.15
print('Para pasajes destinas: ' + str(pasajes))

#Boletos_cine equivale al 10% del salario
boletos_cine = salario * 0.10
print('Para boletos destinas: ' + str(boletos_cine))

#Libros equivale al 15% del salario
libros = salario * 0.15
print('Para libros destinas: ' + str(libros))

#El alquiler es igual al restante de todos los valores anteriores
alquiler = salario - (alimentos + pasajes + boletos_cine + libros)
alquiler = round(alquiler, 2)
print('Para el alquiler destinas: {}'.format(alquiler))
