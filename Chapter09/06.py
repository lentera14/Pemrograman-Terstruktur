print(''.ljust(90, '='))
print(''.ljust(90, '='))
awal = 'NIM \t NAMA \t\t\t N.MID \t\t N.UAS \t\t N.AKHIR \t\t STATUS'
print(awal)
print(''.ljust(90, '-'))

nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]

for i in nilai:
    akhir = round((i['mid'] + (2 * i['uas'])) / 3, 2)
    status = 'LULUS'
    if akhir < 60:
        status = 'TIDAK LULUS'
    print(i['nim'].ljust(8), i['nama'].ljust(15),
          str(i['mid']).ljust(11), str(i['uas']).ljust(11),
          str(akhir).ljust(15), status)

print(''.ljust(90, '-'))
