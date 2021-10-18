# Gaji Karyawan

kode = input('Masukkan kode karyawan : ')
nama = input('Masukkan nama karyawan : ')

if (True):
    gol = str(input('Masukkan golongan      : '))
    if (gol == 'A'):
        gp = 4000000
        pot = 2.5
    elif (gol == 'B'):
        gp = 3500000
        pot = 2.0
    elif (gol == 'C'):
        gp = 3000000
        pot = 1.5
    elif (gol == 'D'):
        gp = 2500000
        pot = 1.0

pothsl = round(pot/100 * gp)
gb = (gp-pothsl)

print(' ')
print('=' * 36)
print('STRUK RINCIAN GAJI KARYAWAN')
print('-' * 36)
print('Nama Karyawan          : ' + str(nama) + ' (' + 'Kode: ' + str(kode) + ')')
print('Golongan               : ' + str(gol))
print('-' * 36)
print('Gaji Pokok             : Rp' + str(gp))
print('Potongan('+ str(pot) + '%)         : Rp' + str(pothsl))
print('-' * 36 + ' -')
print('Gaji Bersih            : Rp' + str(gb))
