#Ejercicio18 Calcular el interes segun el monto del credito

monto_credito = int(input('Cuanto deseas que te prestemos en tu credito?: \n'))

if monto_credito > 1000000:
    interes = int(monto_credito * 0.05)
elif monto_credito >= 750000 and monto_credito <= 1000000:
    interes = int(monto_credito * 0.0375)
elif monto_credito >= 500000 and monto_credito <= 7500000:
    interes = int(monto_credito *0.025)
else:
    interes = int(monto_credito * 0.0175)

print(f'El valor del interes para ese credito es de: {interes}')

