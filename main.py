import os # this line imports the os module.
import csv # this line imports the csv module to enable you read csv file

month_count = 0
# the next line loads the csv file "budget_data.csv into the python environment using the os.join method.

x = os.path.join("Resources", "budget_data.csv") # x is holding the file.
month_differences = [] # this is a list but its empty at the moment
net_change_list = []
net_total = 0
max_increase_month = "" # this is a string but it's empty at the moment
max_increase_amount = float("-inf") # the variable will hold any floating point value from -0 to -infinity.
# a negative number you can not tell
min_increase_month = ""
min_increase_amount = float("inf") # from 0 to +ve infinity: a +ve number you cannot tell.

with open(x, "r") as y: # open() is used to open a file.
 # recall that you have created a variable x to hold the d=budget_data file. so you now want to
 # open the file and read it  since "r" mode is specified. but you are using y to hold the data in it.

    budget_data = csv.reader(y) #csv.reader() is a function in the csv module that used to read a csv file.

    header = next(budget_data) # reads the first row of the csv file which is "Date" and "Profit/Loss
    print(header)
    first_row = next(budget_data) # reads the next row after the first row
    month_count += 1 # you have increamented month_count by one. another is
 # month_count = month_count+1
    net_total += int(first_row[1]) # this extracts the 2nd column of the csv file which is Profit/Loss
    # and put it in net_total variable.
    prev_net = int(first_row[1]) # same as line 28
    for i in budget_data: # to traverse over the csv file
        month_count += 1 # increases count of month by 1 after every iteration
        net_total += int(i[1]) # converts the Profit/Loss values into int because,
        # it was read as a string
        net_change = int(i[1]) - prev_net # subtracts the current row frow from the previous row of Profit/Loss.
        prev_net = int(i[1]) # updates the prev_net
        net_change_list += [net_change] # now adds each net_change to the net_change_list
        month_differences += [i[0]] # increaments month_difference by the current Date row
        # Note: this is n not necessary
        if net_change >max_increase_amount: # compares the net_change with max_increase_amount
            max_increase_amount = net_change # if true, max_increase amount becomes the net_change thereby caputing the highest profit
            max_increase_month = i[0] # captures the month of the highest profit

        if net_change < min_increase_amount: # where the first condition is false, it now check if net_change <min_increase_amount
            min_increase_amount = net_change # captures the minimum increase amount.
            min_increase_month = i[0] # captures the date for the min_increase amount.
difference = sum(net_change_list) / len(net_change_list) # calculates the average net_chanage

rounded_difference = round(difference,2) # to get the average in 2 decimal places
# print(f"Total Months:{month_count}")
total_Months = f"Total Months:{month_count}" # string formatting
# print(f"Total: ${net_total}")
total_budget = f"Total: ${net_total}"

# print(f"Average Change: ${rounded_difference}")
average_Monthly_budget_difference =f"Average Change: ${rounded_difference}"

# print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase_amount})")
highest_profit =f"Greatest Increase in Profits: {max_increase_month} (${max_increase_amount})"

# print(f"Greatest Decrease in Profits: {min_increase_month} (${min_increase_amount})")
lowestProfit =f"Greatest Decrease in Profits: {min_increase_month} (${min_increase_amount})"
# print("Results exported to budget_analysis.txt")
description ="The following information shows the results of the analysis of the budget dataset."
results =f" {description}\n\n{total_Months} \n {total_budget} \n {average_Monthly_budget_difference}\n {highest_profit}\n {lowestProfit}"

result_info = os.path.join("Analysis/") # to export analysis results to the budget_analysis text file.
with open("Analysis/budget_analysis.txt","w") as budget_analysis:
    budget_analysis.write(results)
# print(result_info)








