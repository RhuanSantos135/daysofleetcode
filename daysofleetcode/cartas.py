while True:
    n = int(input())

    if n == 0:
        break

    cartas = [i for i in range(n, 0, -1)]
    cartas_descartadas = []

    while len(cartas) >= 2:
        print(cartas)
        cartas_descartadas.append(cartas.pop())
        cartas.insert(0, cartas.pop())
    
    
    print('Cartas descartadas: ' + ','.join(map(str, cartas_descartadas)))
    print(f'Carta remanecente: {cartas[0]}')