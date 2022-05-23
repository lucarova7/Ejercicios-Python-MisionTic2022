#Ejercicio16 Calcular descuentos por kg de manzanas compradas

#0-2 0% 2.01-5 10% 5.01-10 15% 10.01-< 20%

kg_manzanas = float(input('Cuantos Kg de manzanas vas a comprar?: \n'))
valorkg_manzanas = int(kg_manzanas * 2000)

if kg_manzanas < 2.01:
    print('No tienes ningun descuento\n')
    print(f'debes pagar {valorkg_manzanas}\n')
elif kg_manzanas > 2 and kg_manzanas < 5.01:
    print(f'Tienes un descuento del 10%: {valorkg_manzanas*0.10}\n')
    print(f'Debes pagar {valorkg_manzanas-(valorkg_manzanas*0.10)}\n')
elif kg_manzanas > 5 and kg_manzanas < 10.01:
    print(f'Tienes un descuento del 15%: {valorkg_manzanas*0.15}\n')
    print(f'Debes pagar {valorkg_manzanas-(valorkg_manzanas*0.15)}\n')
elif kg_manzanas > 10:
    print(f'Tienes un descuento del 20%: {valorkg_manzanas*0.20}\n')
    print(f'Debes pagar {valorkg_manzanas-(valorkg_manzanas*0.20)}\n')
else:
    print('Escribe cuantos Kg vas a comprar...')
