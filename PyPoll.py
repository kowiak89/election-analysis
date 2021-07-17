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

# Set total_votes = 0
total_votes = 0
# Create a blank list to add the candidates to
candidate_options = []
# Create a blank dictionary to add candidates and votes
candidate_votes = {}
# Create a blank dictionary to add candidates and vote percentages
vote_percentage = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the file
with open(file_to_load) as election_data: # Opens a file without using open/close()

# Preform Analysis
# Read the data with reader
    file_reader = csv.reader(election_data) # Reads the csv file
    
    headers = next(file_reader) # reads the headers of the data

    for row in file_reader: # Iterate through each row of the data 
        total_votes += 1 # Increase the number of total_votes by 1
        candidate_name = row[2] # Find the candidates names
        
        # If candidate name is not already added to the list of candidates then add it
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0 # Set the candidates votes to 0
        candidate_votes[candidate_name] += 1 # Add 1 vote each time a candidate name appears
   
with open(file_to_save, "w") as txt_file:  

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes)/float(total_votes) * 100

        candidate_results = (
            f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

