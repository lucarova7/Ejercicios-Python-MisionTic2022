# Crear una función para evaluar un número y realizar la operación de
# acuerdo a las siguientes condicionales: sí el número (argumento de
# entrada) es menor igual a 15 realice la operación 15-n; sino realice la
# siguiente operación: (15-n)*2

def eval(n=int()):
    if n <= 15:
        operacion = 15 - n
    else:
        operacion = (15 - n) * 2
    
    return operacion

print(eval())
