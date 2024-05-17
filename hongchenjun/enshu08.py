def square(i):
    print(i ** 2)

def mul(a, *args):
    result = a
    for b in args:
        result *= b
    return result

print(mul(2, 4, 6))

def powerr(n):
    def inner(x):
        return x ** n
    return inner
power3 = powerr(3)
power4 = powerr(4)

print(power3(2))
print(power4(3))


def filter_even_numbers(a):
    for i in a:
        if i % 2 == 0:
            print(i)



def factorial(x):
    i = 1
    for j in range(1, x+1):
        i = i * j
    result = i
    return result
print(factorial(5))



sum = 0
while True:
    s = input('plesase')
    num = int(s)
    pre = sum
    sum = sum + num
    print(str(pre)+'+'+str(num)+'=>'+str(sum))







