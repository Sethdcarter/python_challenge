# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast


# Define lists and dictionaries to track candidate names and vote counts


# Winning Candidate and Winning Count Tracker
vote_tracker = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes = total_votes + 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate in vote_tracker:
            vote_tracker[candidate] = vote_tracker[candidate] + 1

        # Add a vote to the candidate's count
        else:
            vote_tracker[candidate] = 1

# Open a text file to save the output
#with open(file_to_output, "w") as txt_file:
winner = max(vote_tracker, key = vote_tracker.get)
max_votes = vote_tracker[winner]

output = [
    f"\nElection Results",
    f"-------------------------",
    f"Total Votes: {total_votes}",
    f"-------------------------",
]


    
    # Print the total vote count (to terminal)
for candidate, votes in vote_tracker.items():
    perc = "{:.3f}%".format(votes/total_votes*100)
    output.append(f"{candidate}: {perc} ({votes})")
output.extend([
    f"-------------------------",
    f"Winner: {winner}",
    f"-------------------------"
])


with open(file_to_output, "w") as txt_file:
    for line in output:
        print(line)
        txt_file.write(line + "\n")
    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
