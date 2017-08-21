
filename = "port-harcourt-weather.txt"

def weatherReport():
	with open(filename) as report:     # open the problem file as report.
		report.next()           # skipping the first and second lines since they are not needed 
		report.next()           # for our analysis.
		dayList = []
		dailyTempSpread = []
		for line in report:
			line.strip()
			line = line.split()
			try:
				dayListNum = int(line[0])   # Attempt to cast the values as integers for easy analysis.
				dailyHigh = int(line[1])
				dailyLow = int(line[2])
			except Exception as e:
				pass
			dailyTempSpread.append(dailyHigh - dailyLow)  # Appending the differences to the created list,
			dayList.append(dayListNum)                    # and the the day numbers.
		#print dailyTempSpread
	dictWeather = dict(zip(dayList, dailyTempSpread))  # A dictionary mapping the day numbers with their temperature spread.
	lowestDay = min(dictWeather, key=dictWeather.get)  # Day with the lowest temperature spread.
	lowestTemp = min(sorted(dictWeather.values()))     # The lowest temperature spread for the month.

	#print lowestDay, lowestTemp
	print "The day with the smallest temperature spread is  day: " + str(lowestDay) + " with temperature spread of " +  str(lowestTemp) + "."

weatherReport()

