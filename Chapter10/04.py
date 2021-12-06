file = open('e:/datamhs.txt', 'r')

nim = []
nama = []
alamat = []
for i in file:
    splt = i.split('|')
    nim.append(splt[0])
    nama.append(splt[1])
    alamat.append(splt[2])

print('Program Pencarian Data Mahasiswa')
print('')

while True:
    cari = input('Masukkan NIM yang ingin dicari: ')
    print('')
    if cari in nim:
        a = nim.index(cari)
        print('Data Mahasiswa')
        print('NIM      : ', nim[a])
        print('Nama     : ', nama[a])
        print('Alamat   : ', alamat[a])
    else:
        print('Data mahasiswa tidak ditemukan')

    lagi = input('Ingin mencari lagi? (y/n): ')
    if lagi == 'y':
        print('')
        continue
    elif lagi == 'n':
        break
