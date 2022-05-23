#EJERCICIO8 Calcular la nota final segun las notas ingresadas

# PorcentajeNota1 = 15%
# PorcentajeNota2 = 30%
# PorcentajeNota3 = 25%
# PorcentajeNota4 = 10%
# PorcentajeNota5 = 20%

nota1 = float(input('Ingrese la nota del primer examen: '))
nota2 = float(input('Ingrese la nota del segundo examen: '))
nota3 = float(input('Ingrese la nota del tercer examen: '))
nota4 = float(input('Ingrese la nota del cuarto examen: '))
nota5 = float(input('Ingrese la nota del quinto examen: '))

nota_final = nota1*0.15 + nota2*0.30 + nota3*0.25 + nota4*0.10 + nota5*0.20
nota_final = round(nota_final, 2)

print('La nota final del estudiante es: {}'.format(nota_final))