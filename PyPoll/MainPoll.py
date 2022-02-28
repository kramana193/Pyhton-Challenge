# PyPoll Analysis

# Importing necessary file and os types
import os 
import csv

# Locating budget file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Assinging N=0 to calculate no. of votes

# Using Votes[] as list to capture Voting data 
CandidateOne = []
CandidateTwo = []
CandidateThree = []

# Reading the csv file and removing header row
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    # For Loop and if Loop to Count the total Number of votes 
    for row in csvreader:
        if row[2] == "Charles Casper Stockham":
            CandidateOne.append(row[2])
        elif row[2] == "Diana DeGette":
            CandidateTwo.append(row[2])
        elif row[2] == "Raymon Anthony Doane":
            CandidateThree.append(row[2])

# If Loop to determine the Winner
if len(CandidateOne) > len(CandidateTwo) and len(CandidateOne) > len(CandidateThree):
    Winner = CandidateOne[1]
elif len(CandidateTwo) > len(CandidateThree) and len(CandidateTwo) > len(CandidateOne):
    Winner = CandidateTwo[1]
elif len(CandidateThree) > len(CandidateOne) and len(CandidateThree) > len(CandidateTwo):
    Winner = CandidateThree[1]

#VotingPercentage calculation
VotingPercentagex = (len(CandidateOne) / (len(CandidateOne) + len(CandidateTwo) + len(CandidateThree))) * 100
VotingPercentagey = (len(CandidateTwo) / (len(CandidateOne) + len(CandidateTwo) + len(CandidateThree))) * 100
VotingPercentagez = (len(CandidateThree) / (len(CandidateOne) + len(CandidateTwo) + len(CandidateThree))) * 100
TotalVotes = len(CandidateOne) + len (CandidateTwo) + len(CandidateThree)

##### TEST RUNS
#print(TotalVotes)
#print(CandidateOne[1])
#print(CandidateTwo[2])
#print(CandidateThree[3])
#print(str(len(CandidateOne)))
#print(str(len(CandidateTwo)))
#print(str(len(CandidateThree)))
#print(str(Winner))
#print(VotingPercentagex)
#print(VotingPercentagey)
#print(VotingPercentagez)

#from collections import Counter
#Counter(CandidateOne)
#Counter(CandidateTwo)
#Counter(CandidateThree)
#print(Counter(CandidateOne))
#print(Counter(CandidateTwo))
#print(Counter(CandidateThree))

PercentageforC1 = round(VotingPercentagex, 3)
PercentageforC2 = round(VotingPercentagey, 3)
PercentageforC3 = round(VotingPercentagez, 3)

#Print as per Requested Output
file = "Analysis/PyPollAnalysis.txt"
with open(file, 'w') as textfile:
    textfile.write("Election Results\n")
    textfile.write("--------------------------\n")
    textfile.write("Total Votes: %d\n" %TotalVotes)
    textfile.write("--------------------------\n")
    textfile.write(CandidateOne[1] + ": " + str(PercentageforC1) + "% " + "(%s)\n" %len(CandidateOne))  
    textfile.write(CandidateTwo[2] + ": " + str(PercentageforC2) + "% " + "(%s)\n" %len(CandidateTwo))  
    textfile.write(CandidateThree[3] + ": " + str(PercentageforC3) + "% " + "(%s)\n" %len(CandidateThree))
    textfile.write("--------------------------\n")
    textfile.write("Winner: %s\n" %Winner)
    textfile.write("--------------------------\n")


    
#r = single inverted comma for str type, 
#s = for str, 
#d = int(can't handle str) and no decimals, 
#
# Failed = p, n, 
#? = o 