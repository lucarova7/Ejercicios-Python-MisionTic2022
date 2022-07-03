# Crear una función, como argumento de entrada una lista variable de
# argumentos de datos y como resultado, devuelva esa lista en un solo string,
# ejemplo [2,3,4,5,7,11] debe devolver como resultado: 2345711



def lista_to_stri(lista):
    listsalida = ''
    print(type(lista))
    for i in lista:
        listsalida += str(i)
    return listsalida

print(lista_to_stri([2,3,4,5,7,11]))



