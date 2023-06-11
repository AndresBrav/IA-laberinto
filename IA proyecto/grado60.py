def grado60(matriz, inix, iniy, largo):
    for i in range(largo):
        matriz[iniy+i][inix] = 1
        matriz[iniy+i][inix+i] = 1
        matriz[iniy+i][inix+largo-1] = 1
    return matriz

matriz_inicial = [[0] * 20 for _ in range(20)]
inix = 3
iniy = 2
largo = 12

matriz_resultante = grado60(matriz_inicial, inix, iniy, largo)
print(matriz_resultante)


