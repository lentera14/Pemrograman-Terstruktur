buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
print(buah)

nama = input('Nama buah yang dibeli: ')
kg = int(input('Berapa kg            : '))
print('-'*30)
total = buah[nama] * kg
print('Total harga          :', total)
