# 1. list
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

# 2. Menyisipkan nilai pada indesk a 3 dan b 2
a.insert(3, 10)
b.insert(2, 15)
print(a)
print(b)
print('')

# 3. Menyisipkan nilai pada indesk terakhir
a.append(4)
b.append(8)
print(a)
print(b)
print('')

# 4. Melakukan sorting secara ascending
a.sort()
b.sort()
print(a)
print(b)
print('')

# 5. Membuat list c dan list d
c = a[0:8]
d = b[2:10]
print(c)
print(d)
print('')

# 6. List e
e = []
i = 0
for i in range(len(c)):
    f = c[i]+d[i]
    e += [f]
print(e)
print('')

# 7. Ubah list e ke dalam tuple
liste = tuple(e)
print(liste)
print('')

# 8. Mencari nilai min, max, dan jumlah seluruh elemen e
nilaimin = min(liste)
nilaimax = max(liste)
jumlah = sum(liste)
print(nilaimin)
print(nilaimax)
print(jumlah)
print('')

# 9. Membuat sebuah string
myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)
print('')

# 10. Menentukan karakter huruf yang terdapat pada string
huruf = set(myString)
print(huruf)
print('')

# 11. Mengubah string ke list lalu diurutkan
liststr = list(huruf)
liststr.sort()
print(liststr)
