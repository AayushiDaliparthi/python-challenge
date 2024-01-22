# Import dependencies
import os
import csv
from collections import Counter

# Define variables
voters_candidates = []

# Path to collect data from the Resources folder
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    csv_header = next(csv_reader)

    # Read through each row after header
    for row in csv_reader:
        voters_candidates.append(row[2])

# Calculate total votes
total_votes = len(voters_candidates)

# Count votes per candidate
count_candidate = Counter(voters_candidates)

# Get the results in a list of tuples
results = count_candidate.most_common()

# -->>  Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {total_votes}")
print("-------------------------")

# Print each candidate's results
for candidate, votes in results:
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Find the winner
winner = results[0][0]
print("-------------------------")
print(f"Winner:  {winner}")
print("-------------------------")

# Export a text file with the results
election_file = os.path.join("Resources", "election_data.txt")
with open(election_file, "w") as final:
    final.write("Election Results\n")
    final.write("-------------------------\n")
    final.write(f"Total Votes:  {total_votes}\n")
    final.write("-------------------------\n")

    # Write each candidate's results
    for candidate, votes in results:
        percentage = votes / total_votes * 100
        final.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    final.write("-------------------------\n")
    final.write(f"Winner:  {winner}\n")
    final.write("-------------------------\n")
