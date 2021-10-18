# Status Kelulusan Ujian Mahasiswa

BhsIndonesia = int(input('Masukkan nilai Bhs Indonesia  : '))
IPA = int(input('Masukkan nilai IPA            : '))
Matematika = int(input('Masukkan nilai Matematika     : '))

print(' ')

if (BhsIndonesia >= 60) and (IPA >= 60) and (Matematika > 70):
    print('Status Kelulusan              : LULUS')
else:
    print('Status Kelulusan              : TIDAK LULUS')
