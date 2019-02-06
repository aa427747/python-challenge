# Name:  PyBank
# Created: 2/3/19
# Homework:
#   The Total number of months included in dataset
#   The net total amount of "profit/loss" over the period.
#   The average change in prof/loss over the entire period
#   The greatest increase in profits.
#   The greatest decrease in losses.
# Modules
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#import json

csvpath = os.path.join('budget_data.csv')

counter = 0
profits = 0
average = 0
number = 0
higher = 0
lower = 0
difcount = 0
profits_change = 0
change_tot = 0
plug = 86
months = []
profit = []

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
#    months = list(csvreader)
#    row_count = len(months)
#    print(row_count)
#    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
#def get_average(profit):
#    sum = (profit)
#    average = sum / row_count
#    return average
#avg = get_average()
#print(avg)
    for row in csvreader:
       # Add Date to Date array and Profit/Loss to Profit array
        counter = counter + 1
        profits = int(row[1]) + profits
        if counter > 1:
            profits_change = round(float(row[1]) - float(number),2)
            difcount += (profits_change)  
#        print(difcount) 
#        print(profits_change) 
#        change_tot = round(float(profit_change) + float(change_tot),2)
#        print(change_tot)
#        print(profit_change)        
#        average = round(float(profits_change) / float(counter),2)
#        print(average)
#        average = int(row[1]) / counter
#        if int(row[1]) > higher: 
        if profits_change > higher: 
            higher = profits_change
            higher_month = (row[0])
#        if int(row[1]) < lower: 
        if profits_change < lower: 
            lower = profits_change
            lower_month = (row[0])
        number = float(row[1])     
#    print(profits_change)
    average = round(float(difcount) / (float(counter) - 1),2)
#    print(average)
#    print(profit_change)
# Set variable for output file
output_file = os.path.join("pyBanksmain.txt")
#  Open the output file
#with open(output_file, "w", newline="") as datafile:
with open(output_file, "w") as text_file:
    print(f"""Financial Analysis
------------------
Total Month: {counter}
Total:  ${profits}
Average Change: ${average}
Greatest Increase in Profits: {higher_month} ${higher}
Greatest Decrease in Profits: {lower_month} ${lower}""", file=text_file)

 #       print(counter)
 #       months.append(row[0]) 
 #       profit.append(row[1])
 #      len(profit)
 #      print(*profit, sep='\n')
 #       print(*months, sep='\n')
 #      Average Change = Total in Row 1 / Row 0 count?
 #      Greatest Increase = profit + 1 > profit?
 #      Greatest Decrease = provit + 1 < profit?       
 #       print(months) 
 #       print(profit) 
 #       row_count = len(months)
 #       print(row_count)
 #       print(profit)


#json.dumps([1, 'simple', 'list'])
#'[1, "simple", "list"]'
#json.dump(x, f)
#x = json.load(f)
# Zip lists together
#cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
#output_file = os.path.join("test.txt")
#  Open the output file
#with open(output_file, "w", newline="") as datafile:
#with open(output_file, "w") as text_file:
#    print(f"Financial Analysis \n-----------------\nTotal Months: {counter} \nTotal:  ${profits} \nAverage: ${average}  \nGreatest Increase in Profits: Feb-2012  -($1926159) \nGreatest Decrease in Profits: Sept-2013 (-$2196167) ", file=text_file)
#    writer = csv.writer(datafile)
#    print(text)
#    lines = text.writer(text_file)
#    print(lines)

    # Write the header row
#    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
#                     "Percent of Reviews", "Length of Course"])

# Write in zipped rows
#    writer.writerows(cleaned_csv)
