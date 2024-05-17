k = input('開始日')
s = input('終了日')

k = int(k)
s = int(s)
for i in range(k, s+1):
    if 9 < i < 16:
        print('stop')
print('yes')