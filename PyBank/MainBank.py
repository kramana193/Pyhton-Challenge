# PyBank Analysis

# Importing necessary file and os types
import os 
import csv

# Locating budget file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Using Months as list to capture monthly data as well as calculate the length of the list to count months
Months = []
ProfitorLoss = 0
RevenueChange = []
Date_RevenueChange = []
PrevVal = 0
x = 0
y = 0
N = 0

# Reading the csv file and removing header row
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    first_row = next(csvreader)
    PrevVal = int(first_row[1])
    ProfitorLoss = int(first_row[1])
    N = N + 1

    # Total No. of Months in the Data set - Using for loop to calculate No. of rows
    for row in csvreader:
        N = N + 1
        # calculating Profit or Loss at the end of the period by sumation of the values
        ProfitorLoss += int(row[1])
        Months.append(row[0])
        # AverageChange
        x = int(row[1]) - PrevVal
        RevenueChange += [x]
        y = str(row[0])
        #RevenueChange.append(x)
        Date_RevenueChange.append(y)
        PrevVal = int(row[1])
        
#Greatest increase and decrease  
GreatestIncrease = (max(RevenueChange))
GreatestDecrease = (min(RevenueChange))
GIindex = int(RevenueChange.index(GreatestIncrease))
GDindex = int(RevenueChange.index(GreatestDecrease))
GIDate = (Date_RevenueChange[GIindex])
GDDate = (Date_RevenueChange[GDindex])
AverageChange = sum(RevenueChange)/len(RevenueChange)

##### TEST RUNS
#print(RevenueChange)
#print(Date_RevenueChange)
#print(AverageChange)
#print(str(len(RevenueChange)))
#print(GreatestIncrease)
#print(GreatestDecrease)
#print(GIDate)
#print(GDDate)
#print(str(max(RevenueChange)))
#print(str(min(RevenueChange)))
#print("The total number of months included in the data set " + str(len(Months)))
#print(str(N))
#print("The net total amount of Profit/Losses over the entire period was " + str(ProfitorLoss))
AverageChange = round(AverageChange, 2)

# Printing as per the output Requested
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(N))
print("Total: $" + str(ProfitorLoss))
print("Average Change: " + "$" +  str(AverageChange))
print("Greatest Increase in Profits: " + str(GIDate) + " " + "($" + str(GreatestIncrease) + ")")
print("Greatest Decrease in Profits: " + str(GDDate) + " " + "($" + str(GreatestDecrease) + ")")


file = "Analysis/PyBankAnalysis.txt"
with open(file, 'w') as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("-------------------------------\n")
    textfile.write("Total Months: %d\n" %N)
    textfile.write("Total: $%d\n" %ProfitorLoss)
    textfile.write("Average Change: $%s\n" %AverageChange)
    textfile.write("Greatest Increase in Profits: %s ($%s)\n" %(GIDate, GreatestIncrease))
    textfile.write("Greatest Decrease in Profits: %s ($%s)\n" %(GDDate, GreatestDecrease))


    


