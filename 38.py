# Lê o tamanho do vetor
N = int(input())

# Lê os valores do vetor (como string e converte para lista de inteiros)
valores = list(map(int, input().split()))

# Inicializa o menor valor com o primeiro elemento
menor_valor = valores[0]
posicao = 0

# Percorre o vetor para encontrar o menor valor
for i in range(1, N):
    if valores[i] < menor_valor:
        menor_valor = valores[i]
        posicao = i

# Imprime os resultados
print(f"Menor valor: {menor_valor}")
print(f"Posicao: {posicao}")
