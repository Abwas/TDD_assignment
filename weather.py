filename = "port-harcourt-weather.txt"

def weatherReport():
	with open(filename) as file:
	next(file)
	next(file)
	dayList = []
	dailyTempSpread = []
	for line in file:
		splitted_line = line.split()
		try:
			dayListNum = int(splitted_line[0])
			dailyHigh = int(splitted_line[1])
			dailyLow = int(splitted_line[2])
			#print int(splitted_line[0])
		except Exception as e:
			pass
		dailyTempSpread.append(dailyHigh - dailyLow)
		dayList.append(dayListNum)
	weatherDict = dict(zip(dayList, dailyTempSpread))
	print weatherDict
	return dayList, dailyTempSpread, weatherDict


weatherReport()

