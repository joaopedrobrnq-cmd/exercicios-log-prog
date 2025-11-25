x = int(input())
y = int(input())

# garante que x seja o menor
if x > y:
    aux = x
    x = y
    y = aux

soma = 0
n = x

while n <= y:   # único while permitido
    # soma apenas se nao for múltiplo de 13 
    if n % 13 != 0:
        soma += n
    n += 1

print(soma)
