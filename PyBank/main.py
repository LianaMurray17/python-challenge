# Import os module that has functions to interact with the file system
import os

# Import module for reading CSV files
import csv

#Append file directory and make a complete file path
filepath = os.path.join('Resources','budget_data.csv')

# Create empty lists 
total_months = []
total_profit = []
monthly_profit_change = []

 
# Read in the CSV file
with open(filepath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader: 

        # Append the total months and total profit to their corresponding lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))


    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_profit)-1):
        
        # Take the difference between two months and append to monthly profit change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Find the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 


#Open and read CSV file
with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)

    
#print to Output_Summary 
print("Financial Analysis")
print("\n")
print("----------------------------")
print("\n")
print(f"Total Months: {len(total_months)}")
print("\n")
print(f"Total: ${sum(total_profit)}")
print("\n")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print("\n")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print("\n")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# Output files
output_path = os.path.join('Resources','Output_Summary.txt')


with open(output_path, 'w', newline='') as file:
    
# Write methods to print to Output_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")





























