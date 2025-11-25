while True:
    notas = []
    
    # le até ter só 2 notas válidas
    while len(notas) < 2:
        n = float(input())
        
        if 0 <= n <= 10:
            notas.append(n)
        else:
            print("nota invalida")
    
    media = sum(notas) / 2
    print(f"media = {media:.2f}")
    
    # pergunta se quer novo cálculo
    while True:
        print("novo calculo (1-sim 2-nao)")
        x = int(input())
        
        if x == 1:
            break
        elif x == 2:
            exit()
