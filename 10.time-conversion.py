
timegiven = '07:05:45PM'
time2 = '12:40:22AM'
time3 = '12:45:54PM'
time4 = '12:00:00AM'


def timeConversion(s):

	hour = 0
	hh = int(s[:2])
	mm = int(s[3:5])
	ss = int(s[6:8])
	fh = s[8:]

	if hh >= 1 and hh <= 12 and mm >= 0 and mm <= 59 and ss >= 0 and ss <= 59:
		if fh == 'PM' and hh == 12:
			hour = hh
		elif fh == 'PM' and hh < 12:
			hour = hh + 12
		elif fh == 'AM' and hh == 12:
			hour = 0
		else:
			hour = hh

		hour = str(hour).zfill(2)
		mm = str(mm).zfill(2)
		ss = str(ss).zfill(2)

		print(f'{hour}:{mm}:{ss}')



timeConversion(time4)