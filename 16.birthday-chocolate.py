
li = [1, 2, 1, 3, 2]
d1 = 3
m1 = 2
# r = 2

li2 = [1, 1, 1, 1, 1, 1]
d2 = 3
m2 = 2
# r = 0

li3 = [4]
d3 = 4
m3 = 1
# r = 1

li4 = [4, 5, 4, 5, 1, 2, 1, 4, 3, 2, 4, 4, 3, 5, 2, 2,
       5, 4, 3, 2, 3, 5, 2, 1, 5, 2, 3, 1, 2, 3, 3, 1, 2, 5]
d4 = 18
m4 = 6


def birthday(s, d, m):
    n = len(s)
    print(n)
    counter = 0
    summing = 0
    if n >= 1 and n <= 100 and d >= 1 and d <= 31 and m >= 1 and m <= 12:
        if m == 1 and d == s[0]:
            counter += 1
        elif m == 1 and d != s[0]:
            counter = 0
        else:
            for i in range(n-1):
                if s[i] >= 1 and s[i] <= 5:
                    # amount squares (m) summing (d)   m=2(squares)  = d(3)
                    # show how segments meet the criteria
                    for j in range(m):
                        summing += s[i+j]

                    print(f"************  => sum[i{i}+j{j}] = {summing} ")

                    if summing == d:
                        counter += 1
                    print(f"Sum s[{i}] + s[{i+1}]  = {summing}")

                    summing = 0

    print(counter)


birthday(li4, d4, m4)
