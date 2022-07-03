#Crear una función únicamente para sumar números enteros, use el bloque
# try except y la declaración raise que permite al programador forzar a que
# ocurra una excepción específica. Además, emplee a is instance() función
# devuelve la suma y True si el objeto especificado es del tipo especificado,
# en caso contrario un mensaje “Valores deben ser enteros” y False.

def sumaint(numeros):
    suma = ''
    try:
        for i in numeros:
            if isinstance(i, int) == True:
                suma += i
        print(True, suma)
            else:
                raise ValueError('Valores deben ser enteros')
    except:       

