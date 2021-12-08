import datetime

print('Pendataan Peminjam Buku Perpustakaan')
print('')

data = ''
while True:
    komem = input('Masukkan Kode Member : ')
    namem = input('Masukkan Nama Member : ')
    jubuk = input('Masukkan Judul Buku  : ')

    tapin = datetime.date.today()
    tamak = datetime.timedelta(days=7)
    awpin = str(tapin)
    akpin = str(tapin + tamak)

    form = (komem + '|' + namem + '|' + jubuk + '|' + awpin + '|' + akpin + '\n')
    file = open('e:/pinjaman.txt', 'a')
    file.write(form)
    file.close()

    lagi = input('Ingin Menambahkan Lagi? (y/n): ')
    if lagi == 'y':
        print('')
        continue
    elif lagi == 'n':
        buka = open('e:/pinjaman.txt', 'r')
        print('')
        print('Data Peminjam: ')
        baca = buka.read()
        print(baca)
        buka.close()
        break
