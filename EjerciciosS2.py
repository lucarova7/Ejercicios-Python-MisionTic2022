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

#EJERCICIO5 Identificar si una letra ingresada por el usuario es vocal o no

# letra = input('Ingrese una letra: ')
# vocales = ['a', 'e', 'i', 'o', 'u']

# if len(letra) == 1 and letra in vocales:
#     print('Es vocal')
# elif len(letra) != 1:
#     print('Escriba UNA letra')
# else:
#     print('No es vocal')


#EJERCICIO6 Saber si un año es bisiesto

# año = int(input('Ingrese un año: '))

# if año % 4 == 0 or año % 400 == 0 and año % 100 != 0:
#     print('Es bisiesto')
# else:
#     print('No es bisiesto')

#EJERCICIO7 Saber si un numero ingresado por el usuario es Par o Impar

# numero = int(input('Ingrese un numero: '))

# if numero % 2 == 0:
#     print('Es par')
#     print(numero**2)
# else:
#     print('Impar')
#     print(numero**3)

#EJERCICIO8 Calcular la nota final segun las notas ingresadas

#PorcentajeNota1 = 15%
#PorcentajeNota2 = 30%
#PorcentajeNota3 = 25%
#PorcentajeNota4 = 10%
#PorcentajeNota5 = 20%

# nota1 = float(input('Ingrese la nota del primer examen: '))
# nota2 = float(input('Ingrese la nota del segundo examen: '))
# nota3 = float(input('Ingrese la nota del tercer examen: '))
# nota4 = float(input('Ingrese la nota del cuarto examen: '))
# nota5 = float(input('Ingrese la nota del quinto examen: '))

# nota_final = nota1*0.15 + nota2*0.30 + nota3*0.25 + nota4*0.10 + nota5*0.20
# nota_final = round(nota_final, 2)

# print('La nota final del estudiante es: {}'.format(nota_final))

#EJERCICIO 9 Calcular el impuesto vehicular segun el valor comercial

# valor_vehiculo = int(input('Ingrese el valor del vehiculo sin puntos: '))

# if valor_vehiculo <= 50950000:
#     valor_vehiculo = valor_vehiculo * 0.015
#     valor_vehiculo = round(valor_vehiculo, 0)
#     print('El valor del impuesto a pagar es de: {}'.format(valor_vehiculo))

# elif valor_vehiculo >= 50950000 and valor_vehiculo < 114650000 :
#     valor_vehiculo = valor_vehiculo * 0.025
#     valor_vehiculo = round(valor_vehiculo, 0)
#     print('El valor del impuesto a pagar es de: {}'.format(valor_vehiculo))

# else:
#     valor_vehiculo = valor_vehiculo * 0.035
#     valor_vehiculo = round(valor_vehiculo, 0)
#     print(' El valor del impuesto a pagar es de: {}'.format(valor_vehiculo))

