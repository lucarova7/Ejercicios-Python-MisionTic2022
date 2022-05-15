#Ejercicio15 Ofrecer descuentos por cantidad de computadoras compradas

valor_computadora = 985000
cantidad_computadoras = int(input('Cuantas computadoras vas a comprar?: \n'))
valor_total = valor_computadora * cantidad_computadoras

if cantidad_computadoras < 5:
    print(valor_total - (valor_total*0.10))
elif cantidad_computadoras >= 5 and cantidad_computadoras < 10:
    print(valor_total - (valor_total*0.20))
elif cantidad_computadoras >= 10:
    print(valor_total - (valor_total*0.40))
else:
    print('Ingresa una cantidad: ')

exit()