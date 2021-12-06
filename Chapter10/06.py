file = open('e:/sandicaesar.txt', 'a')

asli = 'SAYA SUKA PYTHON'
lis = list(asli)

n = 2

hasil = ''
for a in asli:
    if a.isalpha():
        sandi = 65 + ((ord(a) % 65) + n) % 26
        hasil += chr(sandi)
    else:
        hasil += ' '

file.write(hasil)
file.close()
