#EJERCICIO7 Saber si un numero ingresado por el usuario es Par o Impar

numero = int(input('Ingrese un numero: '))

if numero % 2 == 0:
    print('Es par')
    print(numero**2)
else:
    print('Impar')
    print(numero**3)