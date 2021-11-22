buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}


while True:
    print('Menu: ')
    print('A. Tambah data buah')
    print('B. Beli buah')
    print('C. Keluar')
    pil = input('Pilihan menu: ')
    if pil == 'A':
        while True:
            nama = input('Masukkan nama buah       : ')
            if nama in buah:
                print('Nama buah sudah ada')
            else:
                harga = int(input('Masukkan harga buah      : '))
                buah[nama] = harga
            lagi = input('Mau menambahkan lagi? (y/n): ')
            if lagi == 'y':
                continue
            elif lagi == 'n':
                for a, b in buah.items():
                    print('-', a, '(Harga Rp ', b, ')')
                break
        print('')
        continue

    if pil == 'B':
        for a, b in buah.items():
            print('-', a, '(Harga Rp ', b, ')')
        hrg = 0
        while True:
            nama = str(input('Nama buah yang dibeli: '))
            if nama in buah:
                kg = int(input('Berapa kg            : '))
                total = buah[nama] * kg
                hrg += total
                lain = input('Beli buah yang lain? (y/n): ')
                if lain == 'y':
                    continue
                elif lain == 'n':
                    print('')
                    print('-' * 40)
                    print('Total harga          :', hrg)
                    break
            else:
                print('Nama buah tidak ada')
        print('')

    if pil == 'C':
        break
