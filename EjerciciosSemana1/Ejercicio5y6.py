#Ejericio5 Convertir grados ingresados por el usuario de Celsius a Fahrenheit.
#Ejercicio6 Convertir de Fahrenheit a Celcius

menu = '''
Elija la conversion de grados que desee: 

[1] Grados Celsius a grados Fahrenheit
[2] Grados Fahrenheit a Celsius

'''
opcion = int(input(menu))

if opcion == 1:
    grados = float(input('Ingrese los grados Celsius: '))
    formula = 9 * grados / 5
    formula = round(formula, 2)
    print('{} grados Celsius equivalen a {} grados Fahrenheit'.format(grados, formula))

elif opcion == 2:
    grados = float(input('Ingrese los grados Fahrenheit: '))
    formula = (grados - 32 / 9) * 5
    formula = round(formula, 2)
    print('{} grados Fahrenheit equivalen a {} grados Celsius'.format(grados, formula))

else:
    print('Ingrese una opcion valida')
