import functools

m = 2
n = 3

aa = [2, 4]
bb = [16, 32, 96]

aa = [2, 6]
bb = [24, 36]

ax = [3, 4]
bx = [24, 48]


aq = [3, 4, 6]
bq = [12, 24, 48]

a = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gcd(x, y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x

    return x


def lcm(x, y):
    return (int(x * y / gcd(x, y)))


def getTotalX(a, b):
    counter = 0

    if len(a) >= 1 and len(b) >= 1 and len(a) <= 10 and len(b) <= 10:
        aLcm = functools.reduce(lambda x, y: lcm(x, y) if (
            x >= 1 and y >= 1 and x <= 100 and y <= 100) else False, a)
        bGcd = functools.reduce(lambda x, y: gcd(x, y) if (
            x >= 1 and y >= 1 and x <= 100 and y <= 100) else False, b)

        for i in range(1, bGcd + 1):
            x = aLcm * i
            if x <= bGcd and x != 0:
                if bGcd % x == 0:
                    counter += 1

        print(counter)


getTotalX(a, b)
