# Lê a operação (S ou M)
O = input().strip()

# Inicializa a matriz 12x12
M = []

# Lê os 144 valores da matriz
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    M.append(linha)

# Calcula a soma dos elementos ABAIXO da diagonal principal
soma = 0
elementos = 0

# A diagonal principal tem índices i == j
# Abaixo da diagonal significa i > j
for i in range(12):
    for j in range(12):
        if i > j:  # Elemento está abaixo da diagonal principal
            soma += M[i][j]
            elementos += 1

# Verifica a operação solicitada
if O == 'S':
    resultado = soma
elif O == 'M':
    resultado = soma / elementos

# Imprime o resultado com 1 casa decimal
print(f"{resultado:.1f}")
