try:
    file = open('e:/data2.txt', 'r')
    sum = 0
    for data in file:
        sum += int(data)
        print(sum)

except ValueError:
    print('input data bukan berupa angka')
