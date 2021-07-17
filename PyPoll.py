# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#open the file
with open(file_to_load) as election_data: # Opens a file without using open/close()

# Preform Analysis
    print(election_data)
# Read the data with reader
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    for row in file_reader: # Print the rows of the data
        print(row)


# open and write to election_analysis
with open(file_to_save, 'w') as txt_file:
    txt_file.write("Counties in the Election")
    txt_file.write('\n-----------------------------')
    txt_file.write("\nArapahoe\nDenver\nJefferson")