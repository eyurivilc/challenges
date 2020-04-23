arreglo2 = [[1,4,2,5],[1,2,4,1],[2,3,3,1],[2,7,7,102]]


arreglo3 = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]




def diagonalDifference(arr):
    left,right,i=0,0,0
    n = len(arr)
    while i != n:
    	if arr[i][i] >= -100 and arr[i][i] <= 100:
	        left+=arr[i][i]
	        print (f"A [{i}][{i}]: {arr[i][i]}")
	        right+=arr[i][n-1-i]
	        print (f"------> B [{i}][{n-1-i}]: {arr[i][n-1-i]}")
	        i+=1
    print (abs(left-right))


diagonalDifference(arreglo3)
