#Ejercicio 4. Calculo de areas y perimetros de figuras geometricas con menu


menu = '''
Elige la figura geometrica de la cual deseas saber su area y perimetro:

[1] Triangulo rectangulo
[2] Rectangulo
[3] Circulo
[4] Cuadrado
[5] Triangulo equilatero

'''

opcion = int(input(menu))

if opcion == 1:
    b = float(input('Ingrese la base: '))
    h = float(input('Ingrese la altura'))
    a = (b*h)/2
    a = round(a, 2)
    p1 = float(input('Ingrese el valor del lado a: '))
    p2 = float(input('Ingrese el valor del lado b: '))
    p3 = float(input('Ingrese el valor del lado c: '))
    p = p1 + p2 + p3
    p = round(p, 2)
    print('El area del triangulo rectangulo es: {}'.format(a))
    print('El perimetro del triangulo rectangulo es: {}'.format(p))