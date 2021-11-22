listx = [5, 2, 6, 8, 14]
b = tuple(listx)


def dataStat(x):
    c = sum(x)/len(x)
    d = max(x)
    e = min(x)
    f = [c, d, e]
    return f


print(dataStat(b))
