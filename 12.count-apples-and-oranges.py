
s = 7
t = 11
a = 5
b = 15
# apples = 3
apples = [-2, 2, 1]
# oranges = 2
oranges = [5, -6]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = len(apples)
    count_oranges = len(oranges)
    d = 0
    apples_sam_house = 0
    oranges_sam_house = 0
    location_apples = []
    location_oranges = []

    if s >= 1 and t >= 1 and a >= 1 and b >= 1 and count_apples >= 1 and count_oranges >= 1 and s <= pow(10, 5) and t <= pow(10, 5) and a <= pow(10, 5) and b <= pow(10, 5) and count_apples <= pow(10, 5) and count_oranges <= pow(10, 5):
        if a < s and s < t and t < b:
            for apple in apples:
                d = a + apple
                location_apples.append(d)
                if d >= pow(-10, 5) and d <= pow(10, 5):
                    for location_apple in location_apples:
                        if location_apple > a and location_apple <= b:
                            apples_sam_house += 1
            for orange in oranges:
                d = b + orange
                location_oranges.append(d)
                if d >= pow(-10, 5) and d <= pow(10, 5):
                    for location_orange in location_oranges:
                        if location_orange > a and location_orange <= b:
                            oranges_sam_house += 1

    print(apples_sam_house)
    print(oranges_sam_house)


countApplesAndOranges(s, t, a, b, apples, oranges)
