file = open('e:/sandicaesar.txt', 'r')
buka = file.readline()
lis = list(buka)

n = 2

teks = ''
for a in lis:
    if a.isalpha():
        sandi = 65 + ((ord(a) % 65) - n) % 26
        teks += chr(sandi)
    else:
        teks += ' '

new = open('e:/asli.txt', 'a')
new.write(teks)
new.close()
