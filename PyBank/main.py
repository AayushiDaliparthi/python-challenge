# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Define variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0

# Path to collect data 
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
             
    # Read through each row after the header
    for row in csv_reader:
        # Count of months
        count_months += 1

        # Net profit loss total
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        # Calculate profit loss change
        if count_months > 1:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)

        # Update previous month to current month
        previous_month_profit_loss = current_month_profit_loss

# Calculate average, highest , lowest
average_profit_loss = round(sum(profit_loss_changes) / (count_months - 1), 2)
highest_change = max(profit_loss_changes)
lowest_change = min(profit_loss_changes)

# best and worst months
best_month = months[profit_loss_changes.index(highest_change)]
worst_month = months[profit_loss_changes.index(lowest_change)]

# Print the analysis 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

# Export a final file with the results
budget_file = os.path.join("Resources", "budget_data.txt")
with open(budget_file, "w") as final:
    final.write("Financial Analysis\n")
    final.write("----------------------------\n")
    final.write(f"Total Months:  {count_months}\n")
    final.write(f"Total:  ${net_profit_loss}\n")
    final.write(f"Average Change:  ${average_profit_loss}\n")
    final.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    final.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")