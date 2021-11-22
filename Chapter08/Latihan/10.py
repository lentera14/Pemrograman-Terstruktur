def modif():
    buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
    print(buah)

    while True:
        new = 0
        nama = input('Nama buah yang dibeli: ')
        kg = int(input('Berapa kg            : '))
        total = buah[nama] * kg
        new += total
        lain = input('Beli buah yang lain? (y/n): ')
        if lain == 'y':
            print('')
            continue
        else:
            print('')
            print('-'*40)
            print('Total harga          :', new)
            break


modif()
