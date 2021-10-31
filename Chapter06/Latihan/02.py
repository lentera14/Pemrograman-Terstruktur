# Bintang 1
def starFormation1(n):
    for d in range(0, n):
        for e in range(0, d + 1):
            print('* ', end='')
        print('\r')


starFormation1(4)
print('')


# Bintang 2
def starFormation2(n):
    for d in range(n, -1, -1):
        for e in range(0, d):
            print('* ', end='')
        print('\r')


starFormation2(4)
print('')


# Bintang 3
def starFormation3(n):
    for d in range(0, n):
        for e in range(0, d+1):
            print('* ', end='')
        print('\r')
    for d in range(n, -1, -1):
        for e in range(0, d-1):
            print('* ', end='')
        print('\r')


starFormation3(7)
