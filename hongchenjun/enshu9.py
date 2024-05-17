def func(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    divisor = 3
    while n != 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 2
    return factors

nanshu = []
for i in range(4000, 5001):
    if i % 17 == 0:
        nanshu.append(i)
print(nanshu)

for num in nanshu:
    factors = func(num)
    print(f"{num}: {factors}")