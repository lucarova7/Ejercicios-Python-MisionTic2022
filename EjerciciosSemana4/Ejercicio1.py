# #Funcion con condicional

# def procesar_paquete(peso, volumen):
#     if peso < 2 and volumen < 0.027:
#         return True
#     else:
#         return False

# print(procesar_paquete(1, 0.01))


#Mejora incluyendo el calculo del volumen

def procesar_paquete(peso):
    alto = float(input('Ingresa el alto del paquete (cm): \n'))
    ancho = float(input('Ingresa el ancho del paquete (cm): \n'))
    profundo = float(input('Ingresa la profundidad del paquete (cm): \n'))
    volumen = (alto * ancho * profundo) / 1000000
    volumen = round(volumen, 2)
    if peso < 50 and volumen < 0.027:
        return print('El paquete si es elegible para envio')
    else:
        return print('El paquete no puede ser enviado')

procesar_paquete(6)
