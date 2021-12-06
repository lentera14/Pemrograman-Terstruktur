file = open('e:/dataangka.txt', 'r')

genap = 0
ganjil = 0

for angka in file:
    if int(angka) % 2 == 0:
        genap += 1
    else:
        ganjil += 1

print('Banyak bilangan genap: ', genap)
print('Banyak bilangan ganjil: ', ganjil)
