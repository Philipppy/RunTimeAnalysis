def check_phone_telemarketers(phone_list,telemarketers):
    #check first column and list all numbers once
    for i in range(len(phone_list)):
        if phone_list[i][0] not in telemarketers:
            telemarketers.append(phone_list[i][0])
    
    'check second column and remove numbers from list'
    'telemarketers because they also receive calls'
    for i in range(len(phone_list)):
        if phone_list[i][1] in telemarketers:
            telemarketers.remove(phone_list[i][1])
            
    return telemarketers

def check_text_telemarketers(phone_list,telemarketers):
    #check first column and list all numbers once
    for i in range(len(phone_list)):
        if phone_list[i][0] in telemarketers:
            telemarketers.remove(phone_list[i][0])
    
    'check second column and remove numbers from list'
    'telemarketers because they also receive calls'
    for i in range(len(phone_list)):
        if phone_list[i][1] in telemarketers:
            telemarketers.remove(phone_list[i][1])
            
    return telemarketers


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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# check calls for numbers that are only on the calling, never on the receiving side
# check texts for number on the texting, but never on the receiving side
telemarketers = []
telemarketers_calls = check_phone_telemarketers(calls, telemarketers)
telemarketers = sorted(check_text_telemarketers(texts,telemarketers_calls))

print("These numbers could be telemarketers:")
for i in range(len(telemarketers)):
    print(telemarketers[i])
    