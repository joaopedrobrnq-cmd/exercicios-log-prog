while True:
    N = int(input())
    if N == 0:
        break
    
    # Construir matriz NxN
    matriz = [[1 for _ in range(N)] for _ in range(N)]
    
    # Preencher os valores
    for i in range(N):
        for j in range(N):
            # Calcula a menor distância até a borda
            # A fórmula: valor = min(i, j, N-1-i, N-1-j) + 1
            # Mas como já inicializamos com 1, só precisamos ajustar se for maior que 1
            distancia_i = min(i, N-1-i)
            distancia_j = min(j, N-1-j)
            valor = min(distancia_i, distancia_j) + 1
            matriz[i][j] = valor
    
    # Imprimir a matriz formatada
    for linha in matriz:
        # Formata cada número com tamanho 3, justificado à direita
        formatada = ' '.join(f"{num:>3}" for num in linha)
        print(formatada.rstrip())  # rstrip para remover espaço no final se houver
    
    print()  # Linha em branco após cada matriz
