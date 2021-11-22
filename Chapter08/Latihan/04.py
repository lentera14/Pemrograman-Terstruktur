sayur = ['bayam', 'kangkung', 'wortel', 'selada']

print('Menu: ')
print('A. Tambahkan data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
print('D. Keluar')

try:
    while True:
        jadi = input('Pilihan Anda: ')
        if jadi == 'A':
            tbh = input('Masukkan nama sayur yang akan ditambahkan: ')
            sayur.append(tbh)
        if jadi == 'B':
            hps = input('Masukkan nama sayur yang akan dihapus: ')
            sayur.remove(hps)
        if jadi == 'C':
            print(sayur)
        if jadi == 'D':
            break
except ValueError:
    print('Nama tidak terdapat dalam data')
