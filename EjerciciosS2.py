#EJERCICIO1 - Ordenar ascendentemente 3 numeros dados por el usuario

numero1 = int(input('Ingrese el primer numero: '))
numero2 = int(input('Ingrese el segundo numero: '))
numero3 = int(input('Ingrese el tercer numero: '))

a = min(numero1, numero2, numero3)
b = max(numero1, numero2, numero3)
c = (numero1 + numero2 + numero3) - a - b
print('Los numeros ordenados ascendentemente son: {}, {}, {}'.format(a, c, b))