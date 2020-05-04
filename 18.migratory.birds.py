
arr1 = [1, 1, 2, 2, 3]
arr2 = [1, 4, 4, 4, 5, 3]
arr3 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]


def migratoryBirds(arr):
    n = len(arr)
    counter = 0
    index = 1
    typeOfBirds = []
    while index <= 6:
        for i, num in enumerate(arr):
            #print(f'i={i+1}, num={num}')
            if index == num:
                counter += 1
                # print(f'index={index}')
        typeOfBirds.append(counter)
        index += 1
        counter = 0

    # print(typeOfBirds)
    commonBirds = []
    for j in range(6):
        maxValue = max(typeOfBirds)
        if maxValue == typeOfBirds[j]:
            #print(f'j= {j}')
            commonBirds.append(j)
    # print(commonBirds)
    minValue = min(commonBirds) + 1
    print(minValue)


migratoryBirds(arr4)
