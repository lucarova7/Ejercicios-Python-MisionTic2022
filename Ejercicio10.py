#EJERCICIO10 Identificar a que cuadrante del plano cartesiano pertenece un angulo

angulo = int(input('Ingrese el angulo: '))
cuadrante1 = range(0, 91)
cuadrante2 = range(91, 181)
cuadrante3 = range(181, 271)
cuadrante4 = range(271, 361)

if angulo in cuadrante1:
    print('El angulo pertenece al cuadrante I')
elif angulo in cuadrante2:
    print('El angulo pertenece al cuadrante II')
elif angulo in cuadrante3:
    print('El angulo pertenece al cuadrante III')
elif angulo in cuadrante4:
    print('El angulo pertenece al cuadrante IV')
else:
    print('Ingrese un angulo valido')