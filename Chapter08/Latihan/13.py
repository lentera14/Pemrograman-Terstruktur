nilaiMhs = [{'nim': 'A01', 'nama': 'Amir', 'mid': 50, 'uas': 80},
            {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
            {'nim': 'A03', 'nama': 'Cici', 'mid': 50, 'uas': 50},
            {'nim': 'A04', 'nama': 'Dedi', 'mid': 20, 'uas': 30},
            {'nim': 'A05', 'nama': 'Fifi', 'mid': 70, 'uas': 40}]


def nilaiakhir():
    a = 0
    jmlh = len(nilaiMhs)
    for b in range(jmlh):
        akhir = int((nilaiMhs[a]['mid'] + nilaiMhs[a]['uas']*2) / 3)
        nilaiMhs[a]['akhir'] = akhir
        a += 1
    hasil = sorted(nilaiMhs, key=lambda b: b['akhir'], reverse=True)
    print('Nilai Mahasiswa :')
    print(hasil)


nilaiakhir()
