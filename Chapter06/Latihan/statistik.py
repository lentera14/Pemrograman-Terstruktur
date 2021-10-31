def sum(*data):
    j = 0
    for nilai in data:
        j += nilai
    return j


def average(*data):
    j = 0
    for nilai in data:
        j += 1
    total = sum(*data) / nilai
    return total


def maks(*data):
    nilai = max(*data)
    return nilai


def minim(*data):
    nilai = min(*data)
    return nilai
