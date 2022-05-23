#Ejercicio13 Calculadora de aportes al sistema laboral para trabajadores independientes Colombianos

salario = int(input('Ingrese su salario mensual:\n'))

if  salario < 1000000:
    print('Usted no esta obligado a cotizar al sistema de seguridad social!')
    exit()

riesgo = input('Cual es tu nivel de riesgo laboral?:\n')

ibc = float(salario * 0.4)
# ARL = I(0.522%) II(1.044%) III(2.436%) IV(4.350%) V(6.96%)
Salud = int(ibc * 0.125)
Pension =  int(ibc * 0.16)

if riesgo == '1' or 'uno' or 'UNO' or 'I':
    arl = int(ibc * 0.00522)
elif riesgo == '2' or 'dos' or 'DOS' or 'II':
    arl = int(ibc * 0.0144)
elif riesgo == '3' or 'tres' or 'TRES' or 'III':
    arl = int(ibc * 0.02436)
elif riesgo == '4' or 'cuatro' or 'CUATRO' or 'IV':
    arl = int(ibc * 0.04350)
elif riesgo == '5' or 'cinco' or 'CINCO' or 'V':
    arl = int(ibc * 0.0696)
else:
    print('Ingrese un nivel de riesgo valido...')

print(f'Usted debe aportar a Salud {Salud}\n')
print(f'Usted debe aportar a Pension {Pension}\n')
print(f'Usted debe cotizar a ARl {arl}\n')




