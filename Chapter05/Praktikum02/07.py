from random import randint
i = 0
while True:
    bil = randint(0, 10)
    print(bil)
    i += 1
    if bil == 5:
        print('Jumlah perulangan: ' + str(i))
        break
