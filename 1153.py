n = int(input())

fat = 1
contador = n

while contador > 1:
    fat *= contador
    contador -= 1

print(fat)
4
