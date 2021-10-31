# Function Faktorial(n)
def faktorial(n):
    b = 1
    for c in range(1, n + 1):
        b *= c
    print('Hasil Faktorial dari', n, 'adalah', b)


faktorial(5)


# Function Faktorial C
def faktorialC(d, e):
    faktora = 1
    for b in range(1, d + 1):
        faktora *= b
    faktorb = 1
    for c in range(1, e + 1):
        faktorb *= c
    faktorab = 1
    for f in range(1, d - e + 1):
        faktorab *= f
    print('Hasil dari soal Kombinasi', '(', d, ',', e, ')' ' adalah ', faktora / (faktorb * faktorab))


faktorialC(5, 3)


# Function Factorial P
def faktorialP(d, e):
    faktora = 1
    for b in range(1, d + 1):
        faktora *= b
    faktorb = 1
    for c in range(1, e + 1):
        faktorb *= c
    print('Hasil dari soal Permutasi', '(', d, ',', e, ')' ' adalah ', faktora / faktorb)


faktorialP(10, 7)
