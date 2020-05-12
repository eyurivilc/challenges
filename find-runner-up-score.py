if __name__ == '__main__':
    n = 5
    arr = [2, 3, 6, 6, 5]

    maxValue = max(arr)
    while maxValue == max(arr):
        arr.remove(max(arr))

    print(max(arr))
