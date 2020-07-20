# import needed libraries
import os
import csv

# set up counter for calculations
total_votes = 0
khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0
name_list = ["Khan", "Correy", "Li", "O'Tooley"]
vote_total_list = []

# establish filepath and output location
csvpath = os.path.join("Resources", "election_data.csv")

txtoutput = os.path.join("Resources", "Poll_results.txt")

# open csvfile
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #ID and skip header row
    header = next(csvreader)

    #start loop
    for row in csvreader:

        #define row contents as variables
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

        # calculations for total votes
        total_votes += 1

        # conditionals to id votes
        if candidate == "Khan":
            khan_count += 1

        if candidate == "Correy":
            correy_count += 1
        
        if candidate == "Li":
            li_count += 1

        if candidate == "O'Tooley":
            otooley_count += 1

# calculate percentage of the vote
khan_percent = (khan_count / total_votes) * 100
correy_percent = (correy_count / total_votes) * 100
li_percent = (li_count / total_votes) * 100
otooley_percent = (otooley_count / total_votes) * 100

# list amount storage
vote_total_list += [khan_count]
vote_total_list += [correy_count]
vote_total_list += [li_count]
vote_total_list += [otooley_count]

# find winner with max and index
max_value = max(vote_total_list)
max_index = vote_total_list.index(max_value)
winner = name_list[max_index]

# variable for output to save space
output = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"Khan: {khan_percent:.3f}% ({khan_count})\n"
    f"Correy: {correy_percent:.3f}% ({correy_count})\n"
    f"Li: {li_percent:.3f}% ({li_count})\n"
    f"O'Tooley: {otooley_percent:.3f}% ({otooley_count})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n")

# print output variable in command-line
print(output)

#Export analysis to txt file
with open(txtoutput, "w") as txt_file:
    txt_file.write(output)