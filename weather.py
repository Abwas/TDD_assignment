filename = "port-harcourt-weather.txt"

def weatherReport():
	with open(filename) as file:
		next(file)
		next(file)
		dayList = []
		dailyTempSpread = []
		for line in file:
			line = line.split()
			try:
				dayListNum = int(line[0])
				dailyHigh = int(line[1])
				dailyLow = int(line[2])
			except Exception as e:
				pass
			dailyTempSpread.append(dailyHigh - dailyLow)
			dayList.append(dayListNum)
		#print dailyTempSpread
	weatherDict = dict(zip(dayList, dailyTempSpread))
	lowestDay = min(sorted(weatherDict.keys()))
	lowestTemp = min(weatherDict)

	print lowestTemp
	#return dayList, dailyTempSpread, weatherDict



weatherReport()

