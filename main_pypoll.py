# import needed libraries
import os
import csv

# establish filepath
csvpath = os.path.join("Resources", "election_data.csv")

# open csvfile
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

