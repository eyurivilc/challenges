
s = 7 # int, starting point of Sam's house location
t = 11 # int, ending location of Sam's house
a = 5 # int, location of Apple tree
b = 15 # int, location of Orange tree
apples = [-2, 2, 1]  # apples = 3
oranges = [5, -6]  # oranges = 2

def fruits_from(fruits,tree_location):
    d = 0
    fruits_sam_house = 0
    location_fruits = []

    for fruit in fruits:
        d = tree_location + fruit
        if d >= pow(-10, 5) and d <= pow(10, 5):
            location_fruits.append(d)
    
    for location_fruit in location_fruits:
        if location_fruit >= s and location_fruit <= t:
            fruits_sam_house += 1
    
    return fruits_sam_house

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = len(apples)
    count_oranges = len(oranges)

    if s >= 1 and t >= 1 and a >= 1 and b >= 1 and count_apples >= 1 and count_oranges >= 1 and s <= pow(10, 5) and t <= pow(10, 5) and a <= pow(10, 5) and b <= pow(10, 5) and count_apples <= pow(10, 5) and count_oranges <= pow(10, 5):
        if a < s and s < t and t < b:
            apples_sam_house = fruits_from(apples,a)
            oranges_sam_house = fruits_from(oranges,b)

    print(apples_sam_house)
    print(oranges_sam_house)


countApplesAndOranges(s, t, a, b, apples, oranges)
