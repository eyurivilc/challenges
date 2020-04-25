
testgrades = [73, 67, 38, 33]

def gradingStudents (grades):
	fgrades = []

	n = len(grades)

	if n >= 1 and n <= 60:
		for i in range(n):
			if grades[i] >= 0 and grades[i] <= 100:
				if grades[i] < 38:
					fgrades.append(grades[i])
				else:
					next_multiple = lambda n: (int(n/5)+1) * 5
					diff_between = next_multiple(grades[i]) - grades[i]
					if diff_between < 3:
						fgrades.append(next_multiple(grades[i]))
					else:
						fgrades.append(grades[i])

	print(fgrades)

gradingStudents(testgrades)