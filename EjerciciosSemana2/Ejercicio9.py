#EJERCICIO 9 Calcular el impuesto vehicular segun el valor comercial

valor_vehiculo = int(input('Ingrese el valor del vehiculo sin puntos: '))

if valor_vehiculo <= 50950000:
    valor_vehiculo = valor_vehiculo * 0.015
    valor_vehiculo = round(valor_vehiculo, 0)
    print('El valor del impuesto a pagar es de: {}'.format(valor_vehiculo))

elif valor_vehiculo >= 50950000 and valor_vehiculo < 114650000 :
    valor_vehiculo = valor_vehiculo * 0.025
    valor_vehiculo = round(valor_vehiculo, 0)
    print('El valor del impuesto a pagar es de: {}'.format(valor_vehiculo))

else:
    valor_vehiculo = valor_vehiculo * 0.035
    valor_vehiculo = round(valor_vehiculo, 0)
    print(' El valor del impuesto a pagar es de: {}'.format(valor_vehiculo))