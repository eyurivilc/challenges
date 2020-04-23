arreglo = [3,2,1,3]
arreglo2 = [18,90,90,13,90,75,90,8,90,43]


def birthdayCakeCandles(ar):
	n = len(ar)
	
	maxN = 0
	countMax = 0
	
	if n >= 1 and n <= pow(10,5):
		for i in range(n):
			if ar[i] >= 1 and ar[i] <= pow(10,7):
				if ar[i] > maxN:
					maxN = ar[i]

		for j in range(n):	
			if ar[j] == maxN:
				countMax += 1

	print(maxN)
	print(countMax)




birthdayCakeCandles(arreglo2)