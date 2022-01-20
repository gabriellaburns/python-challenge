import os
import csv
import operator
import collections
from collections import Counter

csvpath = os.path.join("/Users/gabriellaburns/Desktop/GT_HW/python-challenge/PyPoll/Resources/election_data.csv")

#variables etc

vote_total = 0
candidate_list = []
candidate_vote_total = {}
candidate_name = []
candidate_vote_percent = {}


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_reader=next(csvreader)

    #total votes and total rows
    for row in csvreader:
        vote_total = vote_total + 1
        #print(len(vote_total))
        candidate_list.append(row[2])
        
        #add 
       
    #convert candidate list to set to get unique values, then back to list 
    candidate_set = set(candidate_list)
    candidate_name =list(candidate_set)
    candidate_vote_total = dict.fromkeys(candidate_name, 0)
    candidate_vote_percent = dict.fromkeys(candidate_name, 0)
    #add names to dictionary 
    
    #calculate vote total for each candidate
    for x in candidate_list:
        if x in candidate_name:
            candidate_vote_total[x] = candidate_vote_total[x] + 1
    
    #calculate vote % for each candidate
    for x in candidate_name:
        candidate_vote_percent[x] = (float(candidate_vote_total[x])/float(vote_total))
    
    #make the percent look prettier
    for key, value in candidate_vote_percent.items():
        candidate_vote_percent[key] = round((value*100),3)
    
    #first we rock the vote, then we sort it from most to least votes
    sorted_candidate_total = dict( sorted(candidate_vote_total.items(), key=operator.itemgetter(1),reverse=True))
    
    #find winner
    winner = max(candidate_vote_total, key=candidate_vote_total.get)

    #print to terminal
    for key in set(candidate_vote_percent.keys()) & set(candidate_vote_total.keys()):
        print(f"{key},: {candidate_vote_percent[key]}%, ({candidate_vote_total[key]})")
#results = dict(candidate_name, candidate_vote_total, candidate_vote_percent)
#print( "totals are :" + str(results))
 


