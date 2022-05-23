#Saber cuantos empleados en cada rango de salario hay y el total de sueldos

contador_1 = 0
contador_2 = 0
gastos = 0 

iterador = 1
n = int(input("Cuántos empleados hay: "))
while iterador<=n:
    sueldo = int(input(f"Ingrese el sueldo de {iterador}: "))
    if sueldo<=300:
        contador_1 +=1
    else:
        contador_2 = contador_2+1    
    gastos = gastos + sueldo
    iterador +=1
print("# de empleados con sueldos menores a 300 ", contador_1)
print("# de empleados con sueldos mayores a 300 ", contador_2)
print("Los gastos por sueldos de la empresa son ", gastos)
