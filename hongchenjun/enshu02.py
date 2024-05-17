print(" ", end="\t")
for j in range(1, 10):
    print(j, end="\t")
print()
for i in range(1, 10):
    print(i, end='\t')
    for j in range(1, 10):

        if (i * j) % 6 == 0:
            print('##', end='\t')
        elif (i * j) % 3 == 0:
            print('@@', end='\t')
        elif (i * j) % 2 == 0:
            print('**', end='\t')
        else:print(i*j, end='\t')
    print()



