# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
avg_change = 0
# Add more variables to track other necessary financial data
avg_change = 0
gr_increase = 0
gr_decrease = 0
increase = 0
prev_row = 0
decrease = 0
first_row = 0
last_row = 0
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    values_list = []

    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months = total_months + 1 

        # Track the net change
        total_net = int(row[1]) + total_net

        # Calculate the greatest increase in profits (month and amount)
        increase = int(row[1]) - int(prev_row)
        if increase > int(gr_increase):
            gr_inc_date = row[0]
            gr_increase = increase

        #prev_row = int(row[1])
            

        # Calculate the greatest decrease in losses (month and amount)
        decrease = int(row[1]) - int(prev_row)
        if decrease < int(gr_decrease):
            gr_dec_date = row[0]
            gr_decrease = decrease

        prev_row = int(row[1])

        values_list.append(int(row[1]))
# Calculate the average net change across the months
avg_change = (values_list[-1] - values_list[0]) / (total_months - 1)
avg_change = round(avg_change, 2)
# Generate the output summary


# Print the output
output = [
f"Financial Analysis",
f"----------------------------",
f"Total Months: {total_months}",
f"Total: ${total_net}",
f"Average Change: ${avg_change}",
f"Greatest Increase in Profits: {gr_inc_date} (${gr_increase})",
f"Greatest Decrease in Profits: {gr_dec_date} (${gr_decrease})"
]
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    for line in output:
        print(line)
        txt_file.write(line + "\n")
