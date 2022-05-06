#Ejercicio 4. Calculo de areas y perimetros de figuras geometricas con menu


menu = int(input('''
Elige la figura geometrica de la cual deseas saber su area y perimetro:

[1] Triangulo rectangulo
[2] Rectangulo
[3] Circulo
[4] Cuadrado
[5] Triangulo equilatero

'''))

if menu == 1:
    b = float(input('Ingrese la base: '))
    h = float(input('Ingrese la altura: '))
    a = (b*h)/2
    a = round(a, 2)
    print('')
    print('El area del triangulo rectangulo es: {}'.format(a))
    print('')
    p1 = float(input('Ingrese el valor del lado a: '))
    p2 = float(input('Ingrese el valor del lado b: '))
    p3 = float(input('Ingrese el valor del lado c: '))
    p = p1 + p2 + p3
    p = round(p, 2)
    print('El perimetro del triangulo rectangulo es: {}'.format(p))
    print('')

elif menu == 2:
    b = float(input('Ingrese la base: '))
    h = float(input('Ingrese la altura: '))
    a = b * h
    a = round(a, 2)
    print('')
    print('El area del rectangulo es: {}'.format(a))
    print('')
    p = 2*b + 2*h
    p = round(p, 2)
    print('El perimetro del rectangulo es: {}'.format(p))
    print('')

elif menu == 3:
    from math import pi
    r = float(input('Ingrese el radio: '))
    a = pi * r**2
    a = round(a, 2)
    print('')
    print('El area del circulo es: {}'.format(a))
    p = 2 * pi * r
    p = round(p, 2)
    print('')
    print('El perimetro del circulo es: {}'.format(p))
    print('')

elif menu == 4:
    l = float(input('Ingrese el valor de uno de los lados: '))
    a = l**2
    a = round(a, 2)
    print('')
    print('El valor del area del cuadrado es: {}'.format(a))
    print('')
    p = l * 4
    p = round(p, 2)
    print('El valor del perimetro del cuadrado es: {}'.format(p))
    print('')

elif menu == 5:
    l = float(input('Ingrese el valor de uno de los lados: '))
    a = l * pow(3,0.5) / 4
    a = round(a, 2)
    print('')
    print('El valor del area del triangulo equilatero es: {}'.format(a))
    print('')
    p = l * 3
    p = round(p, 2)
    print('El valor del perimetro del triangulo equilatero es: {}'.format(p))

else:
    print('Por favor elija una opcion valida')