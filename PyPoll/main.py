# Name:  PyBank
# Created: 2/3/19
# Homework:
#   Total votes cast
#   Complete list of candidates who received votes.
#   Percentage of votes each candidate won.
#   Total nmber of motes each candidate won.
#   Winner of the election based on popular vote.

# Modules
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#import json

csvpath = os.path.join('election_data.csv')

counter = 0
khan = 0
correy = 0
li = 0
otooley = 0


with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    for row in csvreader:
       # Add Date to Date array and Profit/Loss to Profit array
        counter = counter + 1
        if (row[2]) == "Khan":
            khan = khan + 1
#    print(khan)
#        print(len(rows)
        if (row[2]) == "Correy":
            correy = correy + 1
#        print(correy)
        if (row[2]) == "Li":
            li = li + 1
#        print(li)
        if (row[2]) == "O'Tooley":
            otooley = otooley + 1
#        print(otooley)

#    print(counter)
#    print(int(khan) , int(correy) , int(li) , int(otooley))
    pkhan = round((float(khan) / float(counter) * 100),2)
    pcorrey = round((float(correy) / float(counter) * 100),2)
    pli = round((float(li) / float(counter) * 100),2)
    ptooley = round((float(otooley) / float(counter) * 100),2)
#    print("Kahn %.3f%%" % (pkhan), int(khan))
#    print("Correy %.3f%%" % (pcorrey), int(correy))
#    print("Li %.3f%%" % (pli), int(li))
#    print("O'Tooley %.3f%%" % (ptooley), int(otooley))

    if int(khan) >= int(correy) or int(li) or int(otooley):
        winner = "Khan"
    elif int(correy) >= int(li) or int(otooley):
        winner = "Correy"
    elif int(li) >= int(otooley):
        winner = "Li"
    else: 
        winner = "O'Tooley"
#    print(winner)

output_file = os.path.join("vote.txt")
with open(output_file, "w") as text_file:
    print(f"""Election Results
---------------------------------
Total Votes: {counter}
---------------------------------
Khan: {pkhan}%, {khan}
Correy: {pcorrey}%, {correy}
Li: {pli}%, {li}
O'Tooley: {ptooley}%, {otooley}
--------------------------------
Winner: {winner} 
--------------------------------""", file=text_file)