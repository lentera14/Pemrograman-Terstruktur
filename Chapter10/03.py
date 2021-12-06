file = open('e:/datamhs.txt', 'r')
buka = file.readlines()
dataMhs = {}
a = 0

for b in range(len(buka)):
    fix = buka[a]
    data = fix.split('|')
    nim = data[0]
    nama = data[1]
    alamat = data[2].replace('\n', '')
    a += 1
    form = {'nim': nim, 'nama': nama, 'alamat': alamat}
    form2 = {a: form}
    dataMhs.update(form2)

print(dataMhs)
