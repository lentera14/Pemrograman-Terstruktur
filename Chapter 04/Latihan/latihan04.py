import math

print('Kota A ke Kota B')
jarakKotaAkeB = int(input('Jarak dari Kota A ke kota B: '))
kecepatanA = int(input('Keceptan rata-rata: '))
totalA = round((jarakKotaAkeB / kecepatanA) * 60)

print('Kota B ke Kota C')
jarakKotaBkeC = int(input('Jarak dari Kota B ke Kota C: '))
kecepatanB = int(input('Kecepatan rata-rata: '))
totalB = round((jarakKotaBkeC / kecepatanB) * 60)

print('Lama Istirahat')
istirahat = float(input('Lama waktu saat istirahat: '))

print('Waktu Keberangkatan')
jamberangkat = int(input('Angka jam keberangkatan: '))
menitberangkat = int(input('Angka menit keberangkatan: '))
totalC = totalA + totalB + istirahat
totalwaktu = totalC / 60

jamsampai = math.floor(6 + totalwaktu)
menitsampai = math.floor((6 + totalwaktu) % 1 / 0.25 * 15)

print('Pak Amir akan sampai di Kota C pada pukul : ' + str(jamsampai) + ':' + str(menitsampai))
