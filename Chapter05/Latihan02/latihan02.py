# Bilangan Bulat Ganjil
i = 0
j = 0
for k in range(100):
    bil = k + 1
    if bil % 2 == 1:
        i += 1
        j += bil
        print(bil)
    if bil == 99:
        print('Banyaknya bilangan ganjil: ' + str(i))
