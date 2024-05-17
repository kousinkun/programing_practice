prob = 50
money = 4000

if prob > 80:
    print('天気が悪いので本日は家で過ごしましょう')
elif prob > 40 and money > 5000:
    print('雨が降りそうなので今日は映画を見に行きました')
elif prob < 40 and money >5000:
    print('天気がいいので今日は遠出しましょう')
elif prob < 40 and money < 5000:
    print('今日は近場で遊びましょう')

i = 1
j = 0

while i < 100:
        j += i
        i += 2
print(j)

s = 0
for n in range (1, 101, 2):
    s += n
print(s)

i = [i for i in range(1, 11)if i % 2 ==0]

enshu1 = [[1, 22, 3], [22, 3, 4], [10, 2, 4]]

enshu10 = [j for i in enshu1 for j in i if j >= 10]
print(enshu10)



