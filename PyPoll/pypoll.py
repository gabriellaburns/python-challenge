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