from builtins import input

a = input('输入数字1')
b = input('输入数字2')
a = int(a)
b = int(b)
s = [a, b]
n = 0
g = s[n] % s[n + 1]
while g != 0:
    g = (s[n] % s[n + 1])
    n += 1
    s.append(g)

print(s[-2])