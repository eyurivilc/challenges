# Verify if two kangaroos get at the same location & time (return YES or NO)

# x1, v1 int: start position and jump distance for kangaroo 1
# x2, v2 int: start position and jump distance for kangaroo 2

sample1 = [0, 3, 4, 2]
sampleB = [21, 6, 47, 3]

x1 = sample1[0]
v1 = sample1[1]
x2 = sample1[2]
v2 = sample1[3]


sample2 = [0, 2, 5, 3]


def kangaroo(x1, v1, x2, v2):
    i = 0
    if x1 >= 0 and x2 >= x1 and x2 <= 10000 and v1 >= 1 and v2 >= 1 and v1 <= 10000 and v2 <= 10000:
        if v2 > v1:
            print("NO")
        else:
            while x1 < x2:
                i += 1
                x1 += v1
                x2 += v2
                print(f"Step{i} x1: {x1} && x2: {x2} \n")

            else:
                print(x1)
                print("NO")


kangaroo(x1, v1, x2, v2)
