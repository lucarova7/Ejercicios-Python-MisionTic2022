# #EJERCICIO1 - Ordenar ascendentemente 3 numeros dados por el usuario

# numero1 = int(input('Ingrese el primer numero: '))
# numero2 = int(input('Ingrese el segundo numero: '))
# numero3 = int(input('Ingrese el tercer numero: '))

# a = min(numero1, numero2, numero3)
# b = max(numero1, numero2, numero3)
# c = (numero1 + numero2 + numero3) - a - b
# print('Los numeros ordenados ascendentemente son: {}, {}, {}'.format(a, c, b))

# #EJERCICIO2 Ordenar descendentemente usando el codigo anterios

# print('Los numeros ordenados descendentemente son: {}, {}, {}'.format(b, c, a))

#EJERCICIO3 Saber si un numero ingresado por el usuario esta en el rango [-3, 27]

# intervalo = range(-3, 28)

# numero = int(input('Inserte un numero: '))
# if numero in intervalo:
#     print('Este numero si pertenece al intervalo [-3, 27]')
# else:
#     print('Este numero no pertenece al intervalo [-3, 27]')

#EJERCICIO4 Coincidencia en Primera y/o ultima letra de dos nombres

# nombre1 = input('Ingrese el primer nombre: ')
# nombre2 = input('Ingrese el segundo nombre: ')

# if nombre1[0] == nombre2 [0] and nombre1[-1] == nombre2[-1]:
#     print('Coincidencia en la primera y en la ultima letra')
# elif nombre1[0] == nombre2 [0]:
#     print('Coincidencia en la primera letra')    
# elif nombre1[-1] == nombre2[-1]:
#     print('Coincidencia en la ultima letra')
# else:
#     print('No hay coincidencia')