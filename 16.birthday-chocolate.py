
li1 = [1, 2, 1, 3, 2]
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
    counter = 0
    for i, num in enumerate(s):
        print(f"sum: {sum(s[i:i+m])}")
        if sum(s[i:i+m]) == d:
            counter += 1

    print(counter)


birthday(li4, d4, m4)
