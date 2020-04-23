
arreglo = [-4,3,-9,0,4,1]

def plusminus(arr):
	c = len(arr)
	p,n,z = 0,0,0

	if n>=0 and n<=100:
		for i in range(c):
			if arr[i]>=-100 and arr[i]<=100:
				if arr[i] > 0:
					p += 1
				elif arr[i] < 0:
					n += 1
				elif arr[i] == 0:
					z += 1

	l1 = format(p/c, '.6f')
	l2 = format(n/c, '.6f')
	l3 = format(z/c, '.6f')
	

	print (f"{l1}\n{l2}\n{l3}")





plusminus(arreglo)