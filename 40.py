# Lê a coluna C
C = int(input())

# Lê a operação (S ou M)
T = input().strip()

# Inicializa a matriz 12x12
M = []

# Lê os 144 valores da matriz
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    M.append(linha)

# Calcula a soma dos elementos da coluna C
soma = 0
for i in range(12):
    soma += M[i][C]

# Verifica a operação solicitada
if T == 'S':
    resultado = soma
elif T == 'M':
    resultado = soma / 12

# Imprime o resultado com 1 casa decimal
print(f"{resultado:.1f}")
