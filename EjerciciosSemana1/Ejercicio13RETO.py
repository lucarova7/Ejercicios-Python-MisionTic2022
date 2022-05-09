# Calculo de salarios con descuentos de Ley para la Fundacion Efec
#Descuentos: 5% gastos administrativos, 12.5% fondo solidario y 3.5% ARL

hrs_trabajadas = float(input('Ingrese la cantidad de horas trabajadas en el mes: '))
valor_hora = 37000
formula = hrs_trabajadas * valor_hora
descuentos = formula * 0.05 + formula * 0.12 + formula * 0.035
total_pago = formula - descuentos
total_pago = round(total_pago, 0)

print('Usted debe pagarle al trabajador en total: {}'.format(total_pago))
print()
print('De un total neto de {}, se le descontaron al trabajador en conceptos de ley {}'.format(formula, descuentos))