#Ejericio5 Convertir grados ingresados por el usuario de Celsius a Fahrenheit.

grados = float(input('Ingrese los grados Celsius: '))
formula = 9 * grados / 5
grados = round(grados, 2)
formula = round(formula, 2)

print('{} grados Celsius equivalen a {} grados Fahrenheit'.format(grados, formula))
