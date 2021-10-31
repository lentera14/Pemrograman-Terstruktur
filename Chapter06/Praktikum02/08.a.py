def luasSegitiga(a, t):
    luas = a * t / 2
    return luas


alas = 10
tinggi = 20
luassegetiga1 = luasSegitiga(alas, tinggi)
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luassegetiga1)

alas = 15
tinggi = 45
luassegetiga2 = luasSegitiga(alas, tinggi)
print('Luas segitiga dg alas ', alas,
      ' dan tinggi ', tinggi,
      ' adalah ', luassegetiga2)

print('Luas total kedua segitiga di atas adalah ', luassegetiga1 + luassegetiga2)
