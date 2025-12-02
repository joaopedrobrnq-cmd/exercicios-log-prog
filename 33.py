validas = []

while len(validas) < 2:
    nota = float(input())
    
    if 0 <= nota <= 10:
        validas.append(nota)
    else:
        print("nota invalida")

media = sum(validas) / 2
print(f"media = {media:.2f}")
