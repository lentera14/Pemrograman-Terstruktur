# Status Kelulusan Ujian Mahasiswa

BhsIndonesia = int(input('Masukkan nilai Bhs Indonesia  : '))
IPA = int(input('Masukkan nilai IPA            : '))
Matematika = int(input('Masukkan nilai Matematika     : '))

print(' ')

if (BhsIndonesia >= 60) and (IPA >= 60) and (Matematika > 70):
    print('Status Kelulusan              : LULUS')
if (BhsIndonesia < 60) or (IPA < 60) or (Matematika <= 70):
    print('Status Kelulusan              : TIDAK LULUS')

print('Sebab:')
if (BhsIndonesia < 60):
    print('-    Nilai Bahasa Indonesia kurang dari 60')
if (IPA < 60):
    print('-    Nilai IPA kurang dari 60')
if (Matematika <= 70):
    print('-    Nilai Matematika kurang dari 70')
