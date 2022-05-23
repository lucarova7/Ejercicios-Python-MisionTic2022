#Ejercicio4 Calcular total compra x cliente y total recibido


compra_total = 0
valor_kilo = 3000

for i in range(1, 15+1, 1):
    kilos_x_cliente = float(input(f'Cuantos kilos de naranjas va a comprar el cliente {i}: '))
    if kilos_x_cliente > 10:
        total_cliente = (valor_kilo * kilos_x_cliente) * 0.85
    else:
        total_cliente = valor_kilo * kilos_x_cliente
    compra_total = compra_total + total_cliente
    print(f'El cliente {i} debe pagar por su compra: {total_cliente}')

print(f'La tienda recibira por todas la compras: {compra_total}')