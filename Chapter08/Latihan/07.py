buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
item = buah.items()
harga = sorted(item, key=lambda a: a[1], reverse=True)
for b in harga:
    print(b[0])
