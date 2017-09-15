import csv
import random

occupations = {}

percents = []

total = 0.0

with open("occupations.csv", "r") as file:
	reader = csv.reader(file)
	
	#toss out the first row
	reader.next()
	
	for x in reader:
		occupations[x[0]] = float(x[1])
		
		if x[0] != "Total":
			percents.append([float(x[1]), x[0]])
		else:
			total = float(x[1])

for x in range(0, len(percents)):
	percents[x][0] /= total

def sign(x, y):
	if x > y:
		return 1
	return -1

#the idea is to get a cumulative count
percents.sort(sign)
#print percents

#total = occupations["Total"]

for x in range(0, len(percents) - 1):
	percents[x+1][0] += percents[x][0]

#print percents

rand = random.random()

print rand
for x in percents:
	if rand <= x[0]:
		print x[1]
		break

