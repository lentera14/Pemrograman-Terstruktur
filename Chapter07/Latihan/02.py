try:
    nama = input('Masukkan nama file: ')
    file = open(nama, 'a')
    while True:
        data = input('Data yang ingin ditambahkan: ')
        file.write(data)
        lagi = input('Mau menambahkan lagi? (y/n): ')
        if lagi == 'y':
            continue
        else:
            file.close()
        break

except PermissionError:
    print('')
    print('Terdapat Kesalahan Pada Perzinan! Silahkan Memilih Lokasi Lain')
    