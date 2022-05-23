#EJERCICIO3 Saber si un numero ingresado por el usuario esta en el rango [-3, 27]

intervalo = range(-3, 28)

numero = int(input('Inserte un numero: '))
if numero in intervalo:
    print('Este numero si pertenece al intervalo [-3, 27]')
else:
    print('Este numero no pertenece al intervalo [-3, 27]')