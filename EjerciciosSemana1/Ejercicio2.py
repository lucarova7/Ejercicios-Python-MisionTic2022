# Ejercicio 2. Formula de Gauss

print('Calcular la suma de “N” números enteros.')
print('')
numero_enteros = int(input('Ingrese el numero N de enteros: '))
resultado2 = float((numero_enteros**2 + numero_enteros) / 2)
resultado2 = round(resultado2, 2)
print('El resultado de la suma de {} enteros con la formula\n \
de Gauss es igual a: {}'.format(numero_enteros, resultado2))
