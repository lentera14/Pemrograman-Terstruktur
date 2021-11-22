a = int(input('Masukkan jumlah bilangan bulat: '))
b = []
c = 0
for c in range(a):
    d = int(input('Masukkan bilangan bulat: '))
    b.append(d)
    b.sort()
    b.reverse()
print('list: ', b)
