file = open('e:/tambah.txt', 'r')
new = ''
bil1 = []
bil2 = []
a = 0

for b in file:
    splt = b.split('|')
    satu = splt[0]
    dua = splt[1]
    jmlh = int(satu) + int(dua)
    new += str(jmlh) + '\n'

buka = open('e:/hasil.txt', 'w+')
buka.write(new)
buka.close()
