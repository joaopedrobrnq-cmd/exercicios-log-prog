# Lê 10 valores inteiros
X = []
for _ in range(10):
    valor = int(input())
    X.append(valor)

# Substitui valores nulos e negativos por 1
for i in range(10):
    if X[i] <= 0:
        X[i] = 1

# Mostra o vetor formatado
for i in range(10):
    print(f"X[{i}] = {X[i]}")
