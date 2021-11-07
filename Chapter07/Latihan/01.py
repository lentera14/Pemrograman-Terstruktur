try:
    nama = input('Masukkan nama file: ')
    print('Isi file', nama, 'adalah: ')
    file = open(nama, 'r')
    print(file.read())

except FileNotFoundError:
    print('')
    print('Pastikan Lokasi dan Nama File yang Anda Input Sudah Benar!!')
