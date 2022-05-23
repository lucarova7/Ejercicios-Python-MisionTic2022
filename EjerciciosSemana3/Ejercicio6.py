#Calcular resitencia en series

R_SERIE =int(input("¿Cuantas resistencias tiene el circuito? "))
acumulador = 0
inicio = 1
while inicio <= R_SERIE:
    RN_serie =int(input(f"Ingrese el valor de la resistencia {inicio}: "))
    acumulador = acumulador + RN_serie
    inicio +=1
Requivalente_serie = float(acumulador)
print("La r equivalente es {:.2f}".format(Requivalente_serie))    
