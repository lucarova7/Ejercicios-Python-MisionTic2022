#Incluir Funciones

def calcularCosto (alto, ancho, profundo):
    volumen = alto * ancho * profundo
    costo = volumen * 5
    if alto > 30:
        costo = costo + 2000
    if costo > 10000:
            costo = costo + costo*0.19
    return costo
    
def costoTotal (numeroPaquetes, descuento):
    total = 0
    for i in range(numeroPaquetes):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())
        total += calcularCosto (alto, ancho, profundo)
    
    return total*(1-(descuento/100))

costoTotal(2, 1000)