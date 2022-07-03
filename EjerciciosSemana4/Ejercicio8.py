# Crear una función el cual sus argumentos de entrada son: la primera es el
# precio de un producto que contiene el IVA y el segundo argumento es el
# IVA del producto e imprimir el precio del producto sin IVA y el impuesto del
# producto. Ejemplo mifuncion(28100 , 5) resultados: precio sin IVA $ 26762 y
# Impuesto $ 1338. Los dos argumentos y ambos return son datos de tipo
# entero.

def cal_iva(precio=int, iva=int):
    preciowi = int((100 * precio) / 105)
    iva = int(preciowi * 0.05)
    return preciowi, iva

print(cal_iva(28100, 5))