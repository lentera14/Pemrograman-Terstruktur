from random import randint
key = randint(1, 100)

print('                    Hallo!! Selamat Datang!!                     ')
print('Saya telah memilih sebuah bilangan bulat secara acak dari 0 - 100')
print('                      Silahkan ditebak ya!!                      ')

while True:
    ans = input('Tebakan Anda: ')
    if int(ans) < key:
        print('Tebakan Anda Terlalu Kecil')
    if int(ans) > key:
        print('Tebakan Aanda Terlalu Besar')
    if int(ans) == key:
        print('YEAY!! SELAMAT TEBAKAN ANDA BENAR :D')
        break
