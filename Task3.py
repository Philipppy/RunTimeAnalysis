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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#fixed lines ="(0" -> everything in brackets
#mobile = 7 or 8 or 9 and space (after 5 nums) -> first four digits
#Telemarketer = 140 

#print(calls[6][0][:4])
list_of_codes = []
telemar = 0

"TODO: Generalize"
for i in range(len(calls)):
    if calls[i][0][:5] == "(080)":
        #find fixed lines
        if calls[i][1][:2] == "(0":
            stop_pos = calls[i][1].index(')',2,7)
            list_of_codes.append(calls[i][1][:stop_pos+1])
        
        #find mobiles
        elif calls[i][1][0] in ['7','8','9'] and calls[i][1][5] == ' ':
            list_of_codes.append(calls[i][1][:5])
        
        #find telemarketers
        elif calls[i][1][:3] == "140":
            print(calls[i][1][:3])
            list_of_codes.append('140')
        
#TODO sort lexicographic
print(len(list_of_codes)) 
cleaned_list = list(set(list_of_codes))
print(cleaned_list)
                                   
print("The numbers called by people in Bangalore have codes:\n")
for i in range(len(cleaned_list)):
    print(cleaned_list[i])
            