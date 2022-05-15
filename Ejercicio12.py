#EJERCICIO12 Calcular el valor de la matricula con o sin beneficio por promedio

valor_materias = 62000

promedio = float(input('Cual fue el promedio del ultimo periodo: '))
materias = int(input('Cuantas materias va a cursar este periodo: '))
valor_matricula = valor_materias * materias
IVA = valor_matricula * 0.10

if promedio >= 4.5:
    valor_matricula = valor_matricula - valor_matricula*0.30 - IVA
    print('El valor de su matricula con descuentos por promedio es: {}'.format(valor_matricula))
else:
    print('El valor de su matricula sin descuentos es: ' + str(valor_matricula + IVA))