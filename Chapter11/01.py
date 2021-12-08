from datetime import *

print('Program Penghitung Selisih Hari')
print('')

print('Format Penulisan Tanggal "YYYY-MM-DD"')
hariini = datetime.date(datetime.now())
print('Tanggal hari ini:', hariini)

tgl = input('Masukkan tanggal: ')
splt = tgl.split('-')
yyyy = int(splt[0])
mm = int(splt[1])
dd = int(splt[2])
baru = date(yyyy, mm, dd)


def diffDate(x):
    hasil = x - hariini
    return hasil.days


print('Jadi selisih harinya adalah', diffDate(baru), 'hari')
