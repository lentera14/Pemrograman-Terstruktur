file = open('e:/data2.txt', 'r')
sum = 0
for data2 in file:
    sum = sum + int(data2)
print(sum)
