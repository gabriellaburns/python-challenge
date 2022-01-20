import os
import csv
import pathlib


#set path for file 
csvpath = os.path.join("/Users/gabriellaburns/Desktop/GT_HW/python-challenge/PyBank/Resources/budget_data.csv")
file_to_save = os.path.join("analysis", "Financial_Analysis_Summary.txt")

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
    #print(len(total_months)) 

  #change over time

    net_profit = [int(x)for x in net_profit]
    net_profit_sum = sum(net_profit)
    #print(net_profit_sum)
    
    i = 0
    for i in range(len(net_profit)-1):
        monthly_profit_change.append(net_profit[i+1]-net_profit[i])
    # then find the average of those changes
        average_profit_change = round(sum(monthly_profit_change)/len(monthly_profit_change),2)


# Find the greatest increase in profits (date and amount) over the entire period

min_change = min(monthly_profit_change)
max_change = max(monthly_profit_change)


# Find the greatest decrease in profits (date and amount) over the entire period

max_change_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
min_change_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# your final script should both print the analysis to the terminal 

print(f"Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)} ")
print(f"Total: ${net_profit_sum} ")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}") 
print(f"Greatest Increase in Profits: {total_months[max_change_month]} (${(str(max_change))})")
print(f"Greatest Decrease in Profits: {total_months[min_change_month]} (${(str(min_change))})")
# export a text file with the results.

with open(file_to_save,"w") as txt_file:
    pybank_analysis = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {len(total_months)}\n"
        f"Total: ${net_profit_sum}\n"
        f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n"
        f"Greatest Increase in Profits: {total_months[max_change_month]} (${(str(max_change))})\n"
        f"Greatest Decrease in Profits: {total_months[min_change_month]} (${(str(min_change))})\n")
    print(pybank_analysis, end="")

    txt_file.write(pybank_analysis)

