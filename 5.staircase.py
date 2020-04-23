
size = 15


def staircase(n):
	s = ''

	if n>0 and n<=100 and type(n) is int:
		for i in range(n):
			s = ' '*(n-1) + '#'*(i+1) + f" line: {i+1}"
			n -= 1
			print(s)



staircase(size)