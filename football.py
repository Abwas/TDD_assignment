
filename = "football-league-results.txt"

def leagueResult():
	with open(filename) as result:      # open the problem file as result.
		result.next()         # skipping the first line as it is not needed for the analysis.
		goalD = []           # list of goal difference.
		clubNamesList = []   # list of club names/teams.
		for team in result:
			team = team.split()   # splitting the data into list.
			clubData = []        # Initializing lists for the data and teams.
			clubNames = []
			for data in team:          	    # Attempt to extract the integers into the list 'clubData',
				try:                              # and cast others as strings into 'stringData'.
					data = int(data)
					clubData.append(data)
				except ValueError:
					stringData = str(data)
					if stringData != "-":
						clubNames.append(stringData)
					pass
			if len(clubData) > 0:
				goalF = int(clubData[4])      # goalF stands for 'goalFor'.
				goalA = int(clubData[5])      # goalA stands for 'goalAgainst'.
				del clubNames[:1]
				clubNames = " ".join(clubNames)    # joining the splitted club names together.
				clubNamesList.append(clubNames)    # and appending them to a list.
				goalD.append(goalF - goalA)
			#print clubData
			#print clubNames
			#print goalF, goalA, clubNames
			#print clubNamesList, goalD
	teamDict = dict(zip(clubNamesList, goalD))    # A dictionary mapping the teams to their respective goal differences.
	lowestT = min(sorted(teamDict.keys()))        # Sorting the team in the dictionary,
	lowestG = min(sorted(teamDict.values()))      # to get the team with the minimum goal difference.
		
	print "The team with the smallest difference in 'for' and 'against' goals is " + str(lowestT) + ":" + " " + str(lowestG) + "."

leagueResult()