import os
import csv
import collections
from collections import Counter

csvpath = os.path.join("/Users/gabriellaburns/Desktop/GT_HW/python-challenge/PyPoll/Resources/election_data.csv")

#variables etc
vote_total = []
candidate_list = []



with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_reader=next(csvreader)

    #total votes and total rows
    for row in csvreader:
        vote_total.append(row[0])
        #print(len(vote_total))
        candidate_list.append(row[2])
    for i in candidate_list:
        i = 0
        if i = i + 1:
            candidate_votes = .append(candidate_list)

