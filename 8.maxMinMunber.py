arreglo = [12,6,9,5,10,4,20,30,3,33]


def maxMinNumber(arr):
	n = len(arr)
	sum_total, maxN, minN = 0,0,0

	for i in range(n):
		if arr[i] >= 0 and arr[i] <= pow(10,9):
			if arr[i] > maxN:
				maxN = arr[i]
			elif arr[i] < maxN:
				minN = arr[i]

	print(maxN, minN)

maxMinNumber(arreglo)
