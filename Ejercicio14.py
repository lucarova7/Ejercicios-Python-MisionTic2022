#Ejercicio14 Clasificar frecuencia segun longitud de onda captada

lo = float(input('Ingrese la longitud de la onda: \n'))
c = 300000000
frecuencia = c / lo
frecuencia = round(frecuencia, 2)

if frecuencia >=3 and frecuencia <= 30:
    print(f'{frecuencia} Es una frecuencia muy baja')
elif frecuencia >=31 and frecuencia <= 300:
    print(f'{frecuencia} Es una frecuencia baja')
elif frecuencia >=301 and frecuencia <= 3000:
    print(f'{frecuencia} Es una frecuencia media')
elif frecuencia >=3001 and frecuencia <= 30000:
    print(f'{frecuencia} Es una frecuencia alta')
elif frecuencia >=30001 and frecuencia <= 300000:
    print(f'{frecuencia} Es una frecuencia muy alta')
elif frecuencia >=300001 and frecuencia <= 3000000:
    print(f'{frecuencia} Es una frecuencia ultra alta')
elif frecuencia >=3000001 and frecuencia <= 30000000:
    print(f'{frecuencia} Es una frecuencia super alta')
elif frecuencia >=30000001 and frecuencia <= 300000000:
    print(f'{frecuencia} Es una frecuencia extra altas')
else:
    print(f'No hay una categoria para {frecuencia} de frencuencia...\n')

