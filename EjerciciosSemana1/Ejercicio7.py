#Ejercicio7. Convertir segundos a horas, minutos y segundos

segundos = int(input('Ingrese los segundos: '))

horas = segundos // (60*60)
segundos = segundos % (60*60)
minutos = segundos // (60)
segundos = segundos % 60

print('Tu resultado es: {} horas - {} minutos - {} segundos'. format(horas, minutos, segundos))
