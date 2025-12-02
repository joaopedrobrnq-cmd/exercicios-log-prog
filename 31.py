while True:
    m, n = map(int, input().split())
    
    if m <= 0 or n <= 0:
        break
    
    menor = min(m, n)
    maior = max(m, n)
    
    soma = 0
    sequencia = ""
    
    for x in range(menor, maior + 1):
        sequencia += f"{x} "
        soma += x
    
    print(f"{sequencia}Sum={soma}")
