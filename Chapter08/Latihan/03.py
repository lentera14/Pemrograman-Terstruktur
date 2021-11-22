a = int(input('Masukkan Jumlah Mahasiswa: '))
b = []
c = 0
d = 0
for c in range(a):
    e = input('Masukkan Nama Mahasiswa: ')
    b.append(e)
    b.sort()
    c += 1
for d in range(len(b)):
    print(b[d], '(' + str(len(b[d])), 'karakter'+')')
