m = 2
n = 3

aa = [2, 4]
bb = [16, 32, 96]

aa = [2, 6]
bb = [24, 36]

a = [3, 4]
b = [24, 48]


def getTotalX(a, b):
    n = len(a)
    m = len(b)

    if n >= 1 and m >= 1 and n <= 10 and m <= 10:
        for asLcm in range(1, n):
            for bsGcd in range(1, m):
                print(f"a: {a[asLcm]} & b: {b[bsGcd]}")


getTotalX(a, b)
