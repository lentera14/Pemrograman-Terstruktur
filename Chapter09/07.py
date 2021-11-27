print(''.ljust(80, '='))
awal = 'NIM \t NAMA MAHASISWA \t\t TANGGAL LAHIR \t\t TEMPAT LAHIR'
print(awal)
print(''.ljust(80, '-'))

mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR',
       'K004:HENDERY ARKASANA:1999-09-28:JAKARTA',
       'K005:RENDY ANGKASA:2000-03-23:YOGYAKARTA']

for i in mhs:
    split = i.split(':')
    nim = split[0]
    nama = split[1]

    tgllahir = split[2]
    splittgl = tgllahir.split('-')
    tgl = splittgl[2]
    bln = splittgl[1]
    thn = splittgl[0]

    tempatlahir = split[3]
    print(nim.ljust(8), nama.ljust(23), tgllahir.ljust(19), tempatlahir)

print(''.ljust(80, '-'))
