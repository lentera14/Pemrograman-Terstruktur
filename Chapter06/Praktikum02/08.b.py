def luasSegitiga2(alas, tinggi):
    luas = alas * tinggi / 2
    print('Luas segitiga dg alas ', alas,
          ' dan tinggi ', tinggi,
          ' adalah ', luas)


alas = 10
tinggi = 20
luasSegitiga2(alas, tinggi)

alas = 15
tinggi = 45
luasSegitiga2(alas, tinggi)


def total():
    luas = (alas1 * tinggi1 / 2) + (alas2 * tinggi2 / 2)
    print('Luas total kedua segitiga di atas adalah ', luas)


tinggi1 = 20
alas1 = 10
alas2 = 15
tinggi2 = 45
total()
