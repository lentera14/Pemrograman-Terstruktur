bil = [2, 4, 5, 6]
a = tuple(bil)


def kuadrat():
    hasil = []
    for c in range(len(bil)):
        hasil.append(bil[c]**2)
    return hasil


print(kuadrat())
