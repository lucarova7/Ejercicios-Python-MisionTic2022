#Calcular que lista posee mayor valor o igual valor entre dos listas

sumador1= 0
sumador2= 0

acumulador_ = 1
acumulador_2 = 1
print("Cargar la lista 1 ")
while acumulador_ <=15:
    valor1 = int(input(f"Ingrese el valor {acumulador_}: "))
    sumador1 = sumador1+valor1
    acumulador_ +=1

print("Cargar la lista 2 ")
while acumulador_2 <=15:
    valor2 = int(input(f"Ingrese el valor {acumulador_2}: "))
    sumador2 = sumador2+valor2
    acumulador_2 +=1

if sumador1 > sumador2:
    print("Lista 1 tiene un valor acumulador mayor ", sumador1)
else:
    if sumador2 > sumador1:    
        print("Lista 2 tiene un valor acumulador mayor ", sumador2)
    else:
        print("Ambas listas tienen el mismo acumulado ", sumador1 ,  sumador2)    
