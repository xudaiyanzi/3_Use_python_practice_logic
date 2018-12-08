########  HW_3 
########  problem_1 ****************** budget


import os
import csv

csvpath = os.path.join('budget_data.csv')


row_count = 0
total = 0
i = 0
row_change = 0
row_current = 0
row_previous = 0
row_change_sum = 0

greatest_increase = 0
greatest_decrease = 0

with open(csvpath, newline='') as csvfile: 

    scan_row = csv.reader(csvfile,delimiter = ",") 
    
    #skip the head row
    next(scan_row)
    
    #set the loop 
    for row in scan_row:
        
        # to count total row, which include the head
        if len(str(row[0]))!= 0:
            row_count = row_count + 1
        
        # sum the total
        total = total + int(row[1])
        
        #find the change
        i = i + 1
        if i == 1:
            row_previous = int(row[1])
        if i > 1:
            row_current = int(row [1])
            row_change = row_current - row_previous
            row_change_sum = row_change_sum + row_change
            row_previous = row_current
            
            # find the greatest increase
            if greatest_increase < int(row[1]):
                greatest_increase = row_change
                greatest_increase_time = str(row[0])
            
            # find the greatest decrease
            if greatest_decrease > int(row[1]):
                greatest_decrease = row_change
                greatest_decrease_time = str(row[0])
        
    #average the change, I should -1 because there are only row_count-1 changes
    average = row_change_sum / (row_count - 1)

f = open("Pybank-out.txt","w")

print("Financial Analysis",file = f)
print("---------------------", file = f)
print("Total Months:", row_count, file = f)
print("Total: $", total, file = f)
print("Average Change:$",average, file = f)
print("Greatest Increase in Profits:",greatest_increase_time,"(",greatest_increase,")", file = f)
print("Greatest decrease in Profits:",greatest_decrease_time,"(",greatest_decrease,")", file = f)


f.close()

