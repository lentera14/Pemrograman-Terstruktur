print(''.ljust(50, '='))
print(''.ljust(50, '='))
awal = 'NIM \t NAMA \t\t\t N.MID \t\t N.UAS'
print(awal)
print(''.ljust(50, '-'))

nilai = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
         {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
         {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
         {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
         {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]

for i in nilai:
    print(i['nim'].ljust(8), i['nama'].ljust(15), str(i['mid']).ljust(11), str(i['uas']))

print(''.ljust(50, '-'))
