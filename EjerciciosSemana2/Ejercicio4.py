#EJERCICIO4 Coincidencia en Primera y/o ultima letra de dos nombres

nombre1 = input('Ingrese el primer nombre: ')
nombre2 = input('Ingrese el segundo nombre: ')

if nombre1[0] == nombre2 [0] and nombre1[-1] == nombre2[-1]:
    print('Coincidencia en la primera y en la ultima letra')
elif nombre1[0] == nombre2 [0]:
    print('Coincidencia en la primera letra')    
elif nombre1[-1] == nombre2[-1]:
    print('Coincidencia en la ultima letra')
else:
    print('No hay coincidencia')