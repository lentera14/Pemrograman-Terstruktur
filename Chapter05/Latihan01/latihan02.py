# Status Kelulusan Ujian Mahasiswa

BhsIndonesia = int(input('Masukkan nilai Bhs Indonesia  : '))
IPA = int(input('Masukkan nilai IPA            : '))
Matematika = int(input('Masukkan nilai Matematika     : '))

print(' ')

if (BhsIndonesia >= 60) and (IPA >= 60) and (Matematika > 70):
    print('Status Kelulusan              : LULUS')
if (BhsIndonesia < 0) or (IPA < 0) or (Matematika < 0):
    print('Maaf input ada yang tidak valid')
else:
    print('Status Kelulusan              : TIDAK LULUS')
