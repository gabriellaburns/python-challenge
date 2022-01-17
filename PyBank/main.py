import os
import csv
from pathlib import Path 

#set path for file 
csvpath = os.path.join("/Users/gabriellaburns/Desktop/GT_HW/python-challenge/PyBank/Resources/budget_data.csv")
#create column titles for new csv file

total_months = []
net_profit = []
changes = []
average_change = []
average_profit_change = []
monthly_profit_change = []

#find the total number of months included in the dataset

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_reader=next(csvreader)

    for row in csvreader:

        total_months.append(row[0])
        net_profit.append(int(row[1]))
    print(len(total_months)) 

  #change over time

    net_profit = [int(x)for x in net_profit]
    net_profit_sum = sum(net_profit)
    print(net_profit_sum)
    
    i = 0
    for i in range(len(net_profit)-1):
        monthly_profit_change.append(net_profit[i+1]-net_profit[i])
    # then find the average of those changes
        average_profit_change = round(sum(monthly_profit_change)/len(monthly_profit_change),2)


    #for i in range(len(net_profit)-1):
        #monthly_profit_change.append(net_profit[i+1]-net_profit[i])
        #average_profit_change = {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}
        #print(len(average_profit_change))


# Find the greatest increase in profits (date and amount) over the entire period

min_change = min(monthly_profit_change)
max_change = max(monthly_profit_change)


# Find the greatest decrease in profits (date and amount) over the entire period

min_change_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_change_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# your final script should both print the analysis to the terminal 

print(f"Total Months: {len(total_months)} ")
print(f"Total: {net_profit_sum} ")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}") 
print(f"Greatest Increase in Profits: {total_months[max_change_month]} (${(str(max_change))})")
print(f"Greatest Decrease in Profits: {total_months[min_change_month]} (${(str(min_change))})")
# export a text file with the results.

output_file = Path("python-challenge", "PyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)} ")
    file.write("\n")
    file.write(f"Total: {net_profit_sum} ")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}") 
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_change_month]} (${(str(max_change))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[min_change_month]} (${(str(min_change))})")
output_file.close()
