import os
import csv
import collections
from collections import Counter

csvpath = os.path.join("/Users/gabriellaburns/Desktop/GT_HW/python-challenge/PyPoll/Resources/election_data.csv")

#variables etc
vote_total = []
candidate_list = []
candidates = []
candidate_vote_total = []
candidate_vote_percent =[]
candidate_unique = []
winner = []
dic = {}


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_reader=next(csvreader)

    #total votes and total rows
    for row in csvreader:
        vote_total.append(row[0])
        #print(len(vote_total))
    
    #complete list of candidates
    for row in csvreader:
        candidates = (row[2])

    if candidates in candidate_unique:
        candidate_list = candidate_unique.index(candidates)
        candidate_vote_total[candidate_list] = candidate_vote_total[candidate_list] + 1
    else:
        candidate_unique.append(candidates)
        candidate_vote_total.append(1)

percent = []
most_votes = candidate_vote_total[0]
max_index=0

for x in range(len(candidate_unique)):
    candidate_vote_percent = round(candidate_vote_total[x]/len(vote_total)*100,2)
    percent.append(candidate_vote_percent)

    if candidate_vote_total[x] > most_votes:
        most_votes = candidate_vote_total[x]
        max_index = x
winner = candidate_unique[max_index]

print('Election Results')
print(f'Total Votes: {vote_total}')
for x in range(len(candidate_unique)):
    print(f'{candidate_unique[x]} : {percent[x]}% ({candidate_vote_total[x]})')
print(f'Election Winner = {winner}')

