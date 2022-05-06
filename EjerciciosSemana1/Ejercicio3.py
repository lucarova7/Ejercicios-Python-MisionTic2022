#Ejercicio 3. Operaciones basicas de dos numeros con menu

print('Operaciones basicas con dos numeros de entrada')
print('')
numero_entrada1 = float(input('Ingrese el primer numero que desea operar: '))
print('')
numero_entrada2 = float(input('Ingrese el primer numero que desea operar: '))
numero_entrada1 = round(numero_entrada1, 2)
numero_entrada2 = round(numero_entrada2, 2)
menu = '''

Elija que tipo de operacion desea realizar: 
[1] Suma
[2] Resta
[3] Multipliacion
[4] Division

Coloque el numero de la opcion: 
'''
opcion = int(input(menu))

if opcion == 1:
    suma = str(numero_entrada1 + numero_entrada2)
    print('La suma de tus numeros es igual a: ' + suma )
elif opcion == 2:
    resta = str(numero_entrada1 - numero_entrada2)
    print('La resta de tus numeros es igual a: ' + resta)
elif opcion == 3:
    multiplicacion = str(numero_entrada1 * numero_entrada2)
    print('La multiplicacion de tus numeros es igual a: ' + multiplicacion)
elif opcion == 4:
    division = str(numero_entrada1 / numero_entrada2)
    print('La division de tus numeros es igual a: ' + division)
else:
    print('Escriba el numero de una opcion valida Bob')