#EJERCICIO5 Identificar si una letra ingresada por el usuario es vocal o no

letra = input('Ingrese una letra: ')
vocales = ['a', 'e', 'i', 'o', 'u']

if len(letra) == 1 and letra in vocales:
    print('Es vocal')
elif len(letra) != 1:
    print('Escriba UNA letra')
else:
    print('No es vocal')