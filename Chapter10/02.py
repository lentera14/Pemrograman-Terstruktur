data = ''
while True:
    file = open('e:/datamhs.txt', 'a')
    nim = input('Masukkan NIM             : ')
    nama = input('Masukkan Nama Mahasiswa  : ')
    alamat = input('Masukkan Alamat          : ')
    form = nim + '|' + nama + '|' + alamat + '\n'
    lagi = input('Mau menambahkan lagi? (y/n): ')
    if lagi == 'y':
        print('')
        file.write(form)
        file.close()
        continue
    elif lagi == 'n':
        file.write(form)
        file.close()
        break
