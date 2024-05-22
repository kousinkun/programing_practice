import csv
sum = 0
count = 0


sum = 0
with open('../chapter11/sample11_6_1.txt', 'r')as f:
    for line in f:
        line = int(line)
        sum = sum + line
print(sum)


sum = 0
count = 0
with open('../chapter11/sample11_2_1.csv', 'r')as f:
    reader = csv.reader(f)
    for row in reader:
        age = int(row[1])
        sum = sum + age
        count += 1

print(f'{sum/count}')