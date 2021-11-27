def bintang(n):
    jrk = 2 * n - 1
    for a in range(n):
        jmlh = 2 * a + 1
        hasil = '*' * jmlh
        print(hasil.center(jrk))


bintang(4)
