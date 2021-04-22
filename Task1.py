def check_numbers(phone_list,single_nums):
    
    #check first column
    for i in range(len(phone_list)):
        if phone_list[i][0] not in single_nums:
            single_nums.append(phone_list[i][0])
            
    #check second column
    for i in range(len(phone_list)):
        if phone_list[i][1] not in single_nums:
            single_nums.append(phone_list[i][1])
    
    return single_nums
            
    

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


# list every number that is new in list
single_nums =[]

single_nums = check_numbers(texts,single_nums)
single_nums = check_numbers(calls,single_nums)

        
print("There are {} different telephone numbers in the records."
      .format(len(single_nums)))