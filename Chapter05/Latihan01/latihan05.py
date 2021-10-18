# Gaji Karyawan

kode = input('Masukkan kode karyawan              : ')
nama = input('Masukkan nama karyawan              : ')

if (True):
    gol = str(input('Masukkan golongan                   : '))
    sts = str(input('Masukkan status (1: menikah, 2:blm) : '))
    if (sts == '1'):
        ja = str(input('Masukkan jumlah anak                : '))
    elif (sts == '2'):
        ja = 0
        print(' ')

    if (gol == 'A') and (sts == '1'):
        gpk = 4000000
        pot = 2.5
    elif (gol == 'A') and (sts == '2'):
        gpk = 4000000
        pot = 2.5

    if (gol == 'B') and (sts == '1'):
        gpk = 3500000
        pot = 2.0
    elif (gol == 'B') and (sts == '2'):
        gpk = 3500000
        pot = 2.0

    if (gol == 'C') and (sts == '1'):
        gpk = 3000000
        pot = 1.5
    elif (gol == 'C') and (sts == '2'):
        gpk = 3000000
        pot = 1.5

    if (gol == 'D') and (sts == '1'):
        gp = 2500000
        pot = 1.0
    elif (gol == 'D') and (sts == '2'):
        gp = 2500000
        pot = 1.0

    if (sts == '1'):
        ts = round(10 / 100 * gpk)
        ta = round((5 / 100 * gpk) * int(ja))
    else:
        ts = 0
        ta = 0

gk = round(gpk+ts+ta)
pothsl = round(gk*(pot/100))
gb = round(gk - pothsl)

print('=' * 36)
print('STRUK RINCIAN GAJI KARYAWAN')
print('-' * 36)

print('Nama Karyawan          : ' + str(nama) + ' (' + 'Kode: ' + str(kode) + ')')
print('Golongan               : ' + str(gol))
print('Status Menikah         : ' + str(sts))
if (sts == '1'):
    print('Jumlah Anak            : ' + str(ja))
print('-' * 36)
print('Gaji Pokok             : Rp' + str(gpk))
print('Tunjangan Istri/Suami  : Rp' + str(ts))
if (sts == '1'):
    print('Tunjangan Anak         : Rp' + str(ta))
print('-' * 36 + ' +')
print('Gaji Kotor             : Rp' + str(gk))
print('Potongan(' + str(pot) + '%)         : Rp' + str(pothsl))
print('-' * 36 + ' -')
print('Gaji Bersih            : Rp' + str(gb))
