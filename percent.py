import csv

occupations = {}

percents = []

with open("occupations.csv", "r") as file:
	reader = csv.reader(file)
	
	#toss out the first row
	reader.next()
	
	for x in reader:
		occupations[x[0]] = float(x[1])
		
		if x[0] != "Total":
			percents.append(float(x[1]))

#the idea is to get a cumulative count
percents.sort()
print percents

total = occupations["Total"]


