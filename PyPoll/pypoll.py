import os
import csv
import operator
import collections
from collections import Counter

csvpath = os.path.join("/Users/gabriellaburns/Desktop/GT_HW/python-challenge/PyPoll/Resources/election_data.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

#variables 
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
        candidate_list.append(row[2])
       
    #convert candidate list to set to get unique values, then back to list to get a list containing each candidate's name once
    candidate_set = set(candidate_list)
    candidate_name =list(candidate_set)
    candidate_vote_total = dict.fromkeys(candidate_name, 0)
    candidate_vote_percent = dict.fromkeys(candidate_name, 0)
    
    #calculate vote total for each candidate
    for x in candidate_list:
        if x in candidate_name:
            candidate_vote_total[x] = candidate_vote_total[x] + 1
    
    #calculate vote % for each candidate
    for x in candidate_name:
        candidate_vote_percent[x] = (float(candidate_vote_total[x])/float(vote_total))
    
    #make the percent look prettier
    for key, value in candidate_vote_percent.items():
        candidate_vote_percent[key] = round((value*100),4)
    
    #first we rock the vote, then we sort it from most to least votes
    sorted_candidate_total = dict( sorted(candidate_vote_total.items(), key=operator.itemgetter(1),reverse=True))
    sorted_candidate_percent = dict( sorted(candidate_vote_percent.items(), key=operator.itemgetter(1),reverse=True))
 
    winner = max(candidate_vote_total, key=candidate_vote_total.get)
    

    #terminal print out
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {vote_total}")
    print("-------------------------")
    for key in (sorted_candidate_percent.keys()):
       print(f'{key}: {sorted_candidate_percent[key]} ({sorted_candidate_total[key]})')
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

with open(file_to_save, "w") as txt_file:
    #I think this should be right - not sure why it's not working! 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"-------------------------\n"
        for key in (sorted_candidate_percent.keys()):
            f"{key}: {sorted_candidate_percent[key]} ({sorted_candidate_total[key]})\n"
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    print(election_results, end="")

#I also tried this, which brokeon line 88
#output = open("election_results.txt", "w")
#line1 = "Election Results"
#line2 = "--------------------------"
#line3 = str(f"Total Votes: {str(vote_total)}")
#line4 = str("--------------------------")
#output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
#for i in range(len(candidate_name)):
 #   line = str(
  #      f"{candidate_name[i]}: {str(sorted_candidate_percent[i])} ({str(sorted_candidate_total[i])})"
   # output.write('{}\n'.format(line))
#line5 = "--------------------------"
#line6 = str(f"Winner: {winner}")
#line7 = "--------------------------"
#output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
