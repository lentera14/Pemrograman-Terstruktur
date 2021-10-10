print('Awal Rental Mobil')
jamawalrental = int(input('angka jam saat mobil dirental: '))
mntawalrental = int(input('angka menit saat mobil dirental: '))

print('Selesai Rental Mobil')
jamselesairental = int(input('angka jam saat mobil selesai ditental: '))
mntselesairental = int(input('angka menit saat mobil selesai dirental: '))

print('Total Waktu dan Biaya Rental Mobil')
totalwktpermnt = abs((jamawalrental - jamselesairental) * 60) + mntawalrental + mntselesairental
if totalwktpermnt <= 720:
    totalbiaya = 200.000
else:
    totalbiaya = ((totalwktpermnt - 720) / 60 * 10.000) + 200.000

print('Lama waktu mobil dirental ' + str(totalwktpermnt) + 'menit')
print('Total biaya rental yang dibayarkan ' + str(totalbiaya) + ' ribu rupiah')
