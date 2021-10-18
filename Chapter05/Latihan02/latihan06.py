from random import randint
key = randint(1, 100)
scr = 100
print('                    Hallo!! Selamat Datang!!                     ')
print('Saya telah memilih sebuah bilangan bulat secara acak dari 0 - 100')
print('                      Silahkan ditebak ya!!                      ')
print(' ')

while True:
    ans = input('Tebakan Anda: ')
    if int(ans) < key:
        print('Tebakan Anda Terlalu Kecil')
        scr -= 2
    if int(ans) > key:
        print('Tebakan Aanda Terlalu Besar')
        scr -= 2
    if scr <= 0:
        print('Yahhh Anda Kalah :(')
        break
    if int(ans) == key:
        print('YEAY!! SELAMAT TEBAKAN ANDA BENAR :D')
        print(' ')
        print('Nilai Anda: ' + str(scr))
        break
