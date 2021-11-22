myData = ['apel', 'rambutan', 'jeruk']
a = tuple(myData)


def sortStringByChar(b):
    sort = sorted(b, key=len, reverse=True)
    return sort


print(sortStringByChar(a))
