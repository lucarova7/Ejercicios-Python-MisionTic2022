#Calcular las resistencia equivalente de una R ingresada por el usuario

RESISTENCIA = int(input("¿Cuantas resistencias tiene el circuito? "))
b = int(0)
iterador = int(1)
while iterador <=RESISTENCIA:
    RN = int(input(f"Ingrese el valor de la resistencia # {iterador}: "))
    R = (RN**-1)
    b = R+b #acumulador
    iterador +=1
Requivalente = float(b**-1)
print("R equivalente es {:.4f} ".format(Requivalente))   
print("R equivalente es %.2f "%(Requivalente))   

b2 = int(0)
iterador2 = int(1)
#otra alternativa
for i in range(1,RESISTENCIA+1,1): #(inicio,fin, pasos)
    rn =  int(input(f"Ingrese el valor de la resistencia {i}: "))  
    Rn = (rn**-1)
    b2 = Rn + b2
Rtotal = float(b2**-1)
print(f"R equivalente de {i} es %.3f "%(Rtotal))   
