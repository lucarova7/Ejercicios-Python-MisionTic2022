#Calcular la media de 20 temperaturas
temp = int(input('Cuantas temperaturas desea registar?: '))
suma_temp = 0

for i in range(1, temp+1, 1):
    temps = int(input('Ingrese la temperatura: '))
    suma_temp = suma_temp + temps
    prom_temp = suma_temp / temp
print(f'El promedio de las temperaturas ingresadas es de {prom_temp} grados centigrados')
exit()