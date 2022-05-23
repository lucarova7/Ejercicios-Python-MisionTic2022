#Comprobar numero entero ingresado por el usuario
comprobar = True
sucesion=[]
sucesion_par=[]
sucesion_impar=[]

while comprobar == True:
    serie = int(input("Ingrese el valor maximo de la serie: "))
    if serie>0:
        comprobar = False
        resultado_par = float(0)
        resultado_impar = float(0)

        for i in range(1,serie+1,1):
            if i%2  ==0:
                resultado_par += (-1/i)
                sucesion_par.append(resultado_par)
                #sucesion = sucesion+ sucesion_par
            else:
                resultado_impar += (1/i)
                sucesion_impar.append(resultado_impar)
                #sucesion = sucesion+sucesion_impar        
        print("El resultado de la serie par es: %.4f" %(resultado_par))
        print("El resultado de la serie impar es: %.4f" %(resultado_impar))
        sucesion = sucesion_impar+sucesion_par
        print(sucesion)
    else:                
        print("El número es menor o igual a 0. Ingrese nuevamente ")
