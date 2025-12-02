while True:
    X = int(input())
    
    if X == 0:
        break
    
    soma = 0
    pares_encontrados = 0
    
    # Enquanto não encontramos 5 números pares
    while pares_encontrados < 5:
        if X % 2 == 0:  # Se X for par
            soma += X
            pares_encontrados += 1
        X += 1
    
    print(soma)
