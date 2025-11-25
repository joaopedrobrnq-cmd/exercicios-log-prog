n = int(input())

while n > 0:
    x = int(input())
    divisor = 2
    primo = True

    while divisor * divisor <= x:
        if x % divisor == 0:   # 1 if encontrou divisor
            primo = False
            break
        divisor += 1

    if primo:  # 2 if caso seja primo
        print(f"{x} eh primo")
    if not primo:  # 3 if caso não seja primo
        print(f"{x} nao eh primo")

    n -= 1
