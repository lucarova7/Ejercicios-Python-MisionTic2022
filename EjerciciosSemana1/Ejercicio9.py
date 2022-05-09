# Calculo de cesantias con intereses en Colombia

dias_trabajados =int(input('Ingrese los dias trabajados: '))
salario = int(input('Ingrese su salario sin puntos: '))
cesantias = salario * dias_trabajados / 360
cesantias = round(cesantias)
interes_cesantias = cesantias * dias_trabajados * 0.12 / 360
interes_cesantias = round(interes_cesantias)

print('Las cesantias a las que tienes derecho son:  {} pesos colombianos'.format(cesantias))
print('Los intereses de tus cesantias son {} pesos colombianos'.format(interes_cesantias))
