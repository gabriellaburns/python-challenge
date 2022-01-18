import os
import csv
import collections
from collections import Counter
from collections import defaultdict


csvpath = os.path.join("/Users/gabriellaburns/Desktop/GT_HW/python-challenge/PyPoll/Resources/election_data.csv")

#variables etc
vote_total = []
vote_total = 0
candidate_list = []
candidate_vote_total = []
candidate_vote_total = 0
#results = {}


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_reader=next(csvreader)

    #total votes and total rows
    for row in csvreader:
        vote_total = vote_total + 1
        #print(len(vote_total))
        candidate_list.append(row[2])
    
    #convert candidate list to set to get unique values, then back to list 
    candidate_set = set(candidate_list)
    candidate_name =list(candidate_set)

    #calculate vote total for each candidate
    for x in candidate_name:
        if x in candidate_list:
            candidate_vote_total = candidate_vote_total + 1

    results = dict(zip(candidate_name, candidate_vote_total))
    print( "totals are :" + str(results))
   
     #print results
 
    print(candidate_name)
    for x in candidate_name:
        print(f'{candidate_name(x)} : ({candidate_vote_total[x]})') 



