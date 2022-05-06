# Ejercicio 1. Calcular diagonales de un poligono

print("Calcule las diagonales de un poligono con N lados")
print('')
lados_poligono = int(input("Ingrese el numero de lados del poligono: "))
resultado = int(lados_poligono**2 - 3 * lados_poligono) / 2
resultado = str(resultado)
lados_poligono = str(lados_poligono)
print("Las diagonales de un poligono con " + lados_poligono + " lados, son: " + resultado)