from operation import *

a = jumlah(2, 4)
b = kurang(6, 4)
print('a. 2 + 4 * 6 - 4 = ', kali(a, b))

a = jumlah(4, 7)
b = kurang(6, 9)
print('b. (4 + 7) * (6 - 9) = ', kali(a, b))

a = jumlah(2, 4)
b = jumlah(7, 5)
c = kurang(12, 34)
print('c. (10 + 2) / (7 + 5) / (12 - 34) = ', bagi(bagi(a, b), c))
