buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}


def rata():
    jmlh = sum(buah.values())
    ang = len(buah)
    harga = jmlh / ang
    print('Rata-rata harga dari keseluruhan buah yang ada adalah ', harga)


rata()
