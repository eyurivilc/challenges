def diagonalDifference(arr):
    # Write your code here
    total, diagonalA, diagonalB = 0, 0, 0
    size = len(arr)
    print("size:", size)
    for i in range(size):
        for j in range(size):
            if i == j:
                print(f"dA : arr[{i}][{j}]: {arr[i][j]}")
 
            count = (size - 1)
            first = j
            last = count
            if first == (count):
                print(f"dB: arr[{first}][{count}]: {arr[first][count]}")
                last -= 1
        #if arr[i][i] >= -100 and arr[i][i] <= 100:
        '''diagonalA += arr[i][i]
        print("d-A:", arr[i][i])
    
        for j in reversed(range(size)):
            diagonalB += arr[i][j]
            print("d-B ------>", arr[i][j])
        '''
    #total = abs(diagonalA - diagonalB)
    #return total
    #print (total)


#arr = [[11 , 2, 4], [4, 5, 6], [10, 8, -12]]

arr = [[-1,1,-7,-8], [-10,-8,-5,-2], [0,9,7,-1],[4,4,-2,1]]

diagonalDifference(arr)