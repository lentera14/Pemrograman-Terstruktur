file = open('e:/pinjaman.txt', 'r')

komem = []
namem = []
jubuk = []
awpin = []
akpin = []

for pin in file:
    spltpin = pin.split('|')
    komem.append(spltpin[0])
    namem.append(spltpin[1])
    jubuk.append(spltpin[2])
    awpin.append(spltpin[3])
    akpin.append(spltpin[4].strip())

print('Data Pengembalian Buku Perpustakaan')
print('')

while True:
    cari = input('Masukkan Kode Member: ')
    print('')
    if cari in komem:
        data = True
        import datetime

        a = komem.index(cari)
        hariini = datetime.datetime.now()
        from datetime import datetime

        b = akpin[a]
        c = datetime.strptime(b, '%Y-%m-%d')
        hasil = c - hariini
        akhir = datetime.date(hariini)
        batas = datetime.date(c)

        if data:
            d = akhir - batas
            hasil = int(d.days)
            denda = 0
            if e <= 0:
                bayar = 0
            elif e >= 0:
                bayar = 2000 * e
                denda += bayar

            print('Data Peminjam Buku')
            print('Kode Member                  :', komem[a])
            print('Nama Member                  :', namem[a])
            print('Judul Buku                   :', jubuk[a])
            print('Tanggal Mulai Peminjaman     :', awpin[a])
            print('Tanggal Maksimal Peminjaman  :', akpin[a])
            print('Tanggal Pengembalian         :', akhir)
            print('Terlambat                    :', hasil, 'hari')
            print('Denda                        :', 'Rp.', denda)

    else:
        print('Data Tidak Ditemukan')

    print('')
    lagi = input('Ingin Mencari Lagi? (y/n): ')
    if lagi == 'y':
        print('')
        continue
    else:
        break
