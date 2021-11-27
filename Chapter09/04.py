import random


def shuffleString(x, n):
    list = []
    a = 0
    while a < n:
        hasil = ''.join(random.sample(x, len(x)))
        if hasil not in list:
            list += [hasil]
            a += 1
    print(list)


shuffleString('aku', 2)
shuffleString('aku', 3)
shuffleString('aku', 4)
shuffleString('aku', 5)
