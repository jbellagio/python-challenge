import os
import csv

load_file = os.path.join("Resources", "budget_data.csv")

#set-up
total_months = 0
month = []
net_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 100000000000]
total_net = 0

#Read csv
with open(load_file) as budget_data:
    csvreader = csv.reader(budget_data)
    header = next(csvreader)
    
    #data extraction
    first_row = next(csvreader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    for row in csvreader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_list = net_list +[net_change]
        month = month + [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#Get average net change
net_average = sum(net_list) / len(net_list)

#Output file setup
output_file = os.path.join("budget_analysis.txt")

output = (
    f"\nFinancial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_average:.2f}\n"
    f"Greatest Profit Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Profit Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)

#Export
with open(output_file, "w") as txt_file:
    txt_file.write(output)