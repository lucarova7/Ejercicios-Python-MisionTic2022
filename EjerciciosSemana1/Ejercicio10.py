#Hallar la media de dos numeros

from audioop import avg


num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))
avg = (num1 + num2) / 2
print('El promedio de los dos numeros es: %0.2f' %avg)