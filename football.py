filename = "football-league-results.txt"

def leagueResult():
	with open(filename) as result:
		result.next()
		goalD = []           #list of goal difference
		clubNamesList = []   #list of teams
		for team in result:
			team = team.split()
			clubData = []
			clubNames = []
			for data in team:
				try:
					data = int(data)
					clubData.append(data)
				except ValueError:
					stringData = str(data)
					if stringData != "-":
						clubNames.append(stringData)
					pass
			if len(clubData) > 0:
				goalF = int(clubData[4])
				goalA = int(clubData[5])
				del clubNames[:1]
				clubNames = " ".join(clubNames)
				clubNamesList.append(clubNames)
				goalD.append(goalF - goalA)
			#print clubData
			#print clubNames
			#print goalF, goalA, clubNames
		#print clubNamesList, goalD
	teamDict = dict(zip(clubNamesList, goalD))    # A dictionary of teams and goal differences.
	lowestT = min(sorted(teamDict.keys()))        # Sorting the team in the dictionary,
	lowestG = min(sorted(teamDict.values()))      # with the minimum goal difference.
		
	print ("The team with the smallest difference in 'for' and 'against' goals is " + str(lowestT) + ":" + " " + str(lowestG))

leagueResult()