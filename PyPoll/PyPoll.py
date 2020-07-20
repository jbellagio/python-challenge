import os
import csv

load_file = os.path.join("Resources", "election_data.csv")

#set-up
total_votes = 0
candidates = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#Read csv
with open(load_file) as election_data:
    csvreader = csv.reader(election_data)
    header = next(csvreader)
    
    #data extraction
    for row in csvreader:
        print(". ", end=""),

        total_votes = total_votes + 1

        candidate_name = row[2]

        if candidate_name not in candidates:

            candidates.append(candidate_name)

            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Output file setup
output_file = os.path.join("election_analysis.txt")

#Export
with open(output_file, "w") as txt_file:

    output = (
        f"\nElection Analysis\n"
        f"Total Votes: {total_votes}\n"
    )
    print(output, end="")

    txt_file.write(output)

    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        output_2 = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(output_2, end="")

        txt_file.write(output_2)

    output_3 = (
        f"Winner: {winning_candidate}\n"
    )

    print(output_3)
    
    txt_file.write(output_3)
