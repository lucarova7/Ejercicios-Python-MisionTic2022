#EJERCICIO11 Calculo del IMC

peso = float(input('Ingresa tu peso en Kg: '))
altura = float(input('Ingresa tu estatura en mts: '))
IMC = float(peso / altura**2)
IMC = round(IMC, 2)

print('Su IMC es: {}'.format(IMC))

if IMC < 16:
    print('Segun su resultado de IMC sufre usted de Delgadez Severa')
elif IMC in range(16, 17):
    print('Segun su resultado de IMC sufre usted de Delgadez moderada')
elif IMC >= 17 and IMC < 18.50:
    print('Segun su resultado de IMC sufre usted de Delgadez aceptable')
elif IMC >= 18.5 and IMC < 25:
    print('Segun su resultado de IMC usted posee un Peso Normal')
elif IMC >= 25 and IMC < 35:
    print('Segun su resultado de IMC sufre usted de Sobrepeso')
elif IMC >= 30 and IMC < 35:
    print('Segun su resultado de IMC sufre usted de Obesidad tipo I')
elif IMC >= 35 and IMC < 40.01:
    print('Segun su resultado de IMC sufre usted de Obesidad tipo II')
elif IMC >= 40 and IMC < 50:
    print('Segun su resultado de IMC sufre usted de Obesidad tipo III (Obesidad Morbida)')
elif IMC > 50:
    print('Segun su resultado de IMC sufre usted de Obesidad tipo IV o extrema')
else:
    print('Ingrese nuevamente sus datos')