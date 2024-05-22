
import json

sum = 0
cout = 0

with open('../chapter11/sample11_4_1.json', 'r') as f:
    people = json.load(f)
    for person in people:

        sum += person['age']
        cout += 1
print(f'{sum/cout:.1f}')



import xml.etree.ElementTree as et
sum = 0
count = 0

tree = et.parse('../chapter11/sample11_6_1.txt')
root = tree.getroot()
for person in root:
    age = int(person.find('age').txt)
    sum += age
    count += 1
print(f'{sum/count:.1f}')
