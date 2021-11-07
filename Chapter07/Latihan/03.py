print('----- Program Menghitung Rata-Rata -----')
print('')

awal = 0
jmlh = 0

while True:
    try:
        bil = input('Masukkan Bilangan Bulat: ')

        awal += int(bil)
        jmlh += 1
        rata = awal / jmlh

        lagi = input('Mau menambahkan lagi? (y/n): ')
        if lagi == 'y':
            continue
        else:
            print('')
            print('Rata-ratanya adalah: ', rata)
        break

    except ValueError:
        print('Input Bukan Bilangan Bulat!!')

        lagi = input('Mau menambahkan lagi? (y/n): ')
        if lagi == 'y':
            continue
        else:
            print('')
            print('Rata-ratanya adalah: ', rata)
        break
