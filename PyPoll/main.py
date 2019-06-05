# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# Import os module that has functions to interact with the file system
import os

# Import module for reading CSV files
import csv
	
#Get current working directory
cwkdir = os.getcwd()

#Append file directory and make a complete file path
filepath = os.path.join( cwkdir,'Resources','election_data.csv')
	

#Initialize variables
totalcount = 0; khan = 0; correy = 0; li = 0; otooley = 0; max_votecount = 0
	

#Calculate percentage
def percentage (part, whole):
	return 100 * float(part)/float(whole)
	

#Open and read CSV file
with open(filepath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	

	for i in csvreader:
	    voterid = i[0]
	    county = i[1]
	    candidate = i[2]
		
	    # Find Total Vote Count
	    totalcount = totalcount + 1
	

	    # Votecount by candidates
	    if candidate =="Khan":
	        khan = khan + 1
	    if candidate =="Correy":
	        correy = correy + 1
	    if candidate =="Li":
	        li = li + 1
	    if candidate =="O'Tooley":
	        otooley = otooley + 1
	            
# Define (dictionary) list : candidate and votes
	candidatevote = {"Khan": khan,"Correy": correy,"Li" : li, "O'Tooley": otooley}
	# Find winner 
	for candidate, value in candidatevote.items():
	    if value > max_votecount:
	        max_votecount = value
	        winner = candidate
# Display results       
print(f'Election Results'+'\n')
print(f'-------------------------------'+'\n')
print(f'Total Votes: {totalcount}'+'\n')
print(f'-------------------------------'+'\n')
print(f'Khan: {percentage(khan,totalcount):.3f}%  ({khan})')
print(f'Correy: {percentage(correy,totalcount):.3f}%  ({correy})')
print(f'Li: {percentage(li,totalcount):.3f}%  ({li})')
print(f'O\'Tooley: {percentage(otooley,totalcount):.3f}%  ({otooley})')
print(f'--------------------------------'+'\n')
print(f'Winner: {winner} '+'\n')
print(f'--------------------------------'+'\n')


# Output files
output_path = os.path.join('Resources','Output_Summary.txt')


with open(output_path, 'w', newline='') as file:


# Write methods to print to Output_Summary 
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f'Total Votes: {totalcount}'+'\n')
    file.write("\n")
    file.write(f'Khan: {percentage(khan,totalcount):.3f}%  ({khan})')
    file.write("\n")
    file.write(f'Correy: {percentage(correy,totalcount):.3f}%  ({correy})')
    file.write("\n")
    file.write(f'Li: {percentage(lcount,totalcount):.3f}%  ({lcount})')
    file.write("\n")
    file.write(f'O\'Tooley: {percentage(otooley,totalcount):.3f}%  ({otooley})')
    file.write("\n")
    file.write(f'Winner: {winner} '+'\n')




























