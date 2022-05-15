#Plan de reforestacion estado de Mexico

terreno = float(input('Cuantos metros cuadrados tiene el terreno?: \n'))

if terreno > 1000000:
    terreno_pinos = terreno * 0.70
    cantidad_pinos = int((terreno_pinos * 8) / 10)
    terreno_oyamel = terreno * 0.20
    cantidad_oyamel = int((terreno_oyamel * 15) / 15)
    terreno_cedro = terreno * 0.10
    cantidad_cedro = int((terreno_cedro * 10) / 18)
    print(f'''
    Para este terreno debes sembrar:
    {cantidad_pinos} pinos.
    {cantidad_oyamel} oyameles.
    {cantidad_cedro} cedros.

    ''')
else:
    terreno_pinos = terreno * 0.50
    cantidad_pinos = int((terreno_pinos * 8) / 10)
    terreno_oyamel = terreno * 0.30
    cantidad_oyamel = int((terreno_oyamel * 15) / 15)
    terreno_cedro = terreno * 0.20
    cantidad_cedro = int((terreno_cedro * 10) / 18)
    print(f'''
    Para este terreno debes sembrar:
    {cantidad_pinos} pinos.
    {cantidad_oyamel} oyameles.
    {cantidad_cedro} cedros.

    ''')
