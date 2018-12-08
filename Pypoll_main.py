########  HW_3 
########  problem_2 ****************** election


####### Modules

    
import os
import csv
from collections import Counter, defaultdict
    
csvpath = os.path.join('election_data.csv')
row_count = 0
candidate_votes_dict = {}
greatest = 0

with open(csvpath, newline='') as csvfile:
        
    scan_row = csv.reader(csvfile,delimiter = ",")  
    
    #######skip the head row
    next(scan_row)
    
    ########set the loop 
    for row in scan_row:
        
        ##########to count total row, which include the head
        if len(str(row[0]))!= 0:
            row_count = row_count + 1
        
        ######### have a dictionary to store the candidate and its total votes
        if row[2] in candidate_votes_dict:
            candidate_votes_dict[row[2]] = candidate_votes_dict[row[2]] + 1
        
        else:
            candidate_votes_dict[row[2]] = 1
 
    f = open("Pypoll.txt","w")
    
        ########check the dictionary successfully built or not
        ########print(candidate_votes_dict)           
    print("Election Results",file = f)
    print("-----------------------",file = f)
    print ("Total Votes:", row_count,file =f )
    print("-----------------------",file = f)  
    
    
    #######calculate the percentage
    for key,value in candidate_votes_dict.items():
        percent = value/row_count * 100
        if value > greatest:
            winner = key
            greatest = value
        print(key,":","%.3f" % percent,"%","(",value,")", file = f)
        

    print("-----------------------",file = f)
    print("Winner:",winner, file = f)
    print("-----------------------", file = f)
    
    f.close()