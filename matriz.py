vetor = [10, 20, 30, 40, 50]
print(vetor[-1])

matriz = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]

print(matriz[1][2])

# exemplo com notas de alunos

notas_alunos = [
    ['João', 8, 7, 6],
    ['Pedro', 4.5, 9, 10],
    ['Marcos', 6, 6, 8],
]

for linha in notas_alunos:
    for col in linha:
        print(str(col) + '\t', end= " ")
    print('')