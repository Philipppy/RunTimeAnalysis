def check_numbers(phone_list,single_nums):
    
    #check first column
    for i in range(len(phone_list)):
        if phone_list[i][0] not in single_nums:
            single_nums.append(texts[i][0])
            
    #check second column
    for i in range(len(phone_list)):
        if phone_list[i][1] not in single_nums:
            single_nums.append(texts[i][1])
    
    return single_nums

def time_on_phone(single_nums,calls):
    #initialize dict with phone numbers as keys
    time_on_phone = {k:0 for k in single_nums}
    
    for i in range(len(single_nums)):
        for j in range(len(calls)):
            #check if number is in one of the columns and add the time on phone
            if single_nums[i] == calls[j][0] or single_nums[i] == calls[j][1]:
                time_on_phone[single_nums[i]]=int(time_on_phone[single_nums[i]])+int(calls[j][3])
    
    return time_on_phone


"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#create list of all numbers in the file 'calls"
single_nums = []
single_nums = check_numbers(texts,single_nums)

            
#determine the total phone times for each phone number
phone_times = time_on_phone(single_nums,calls)

#get number with highest total time
max_number = max(phone_times, key=phone_times.get)

print("{} spent the longest time, {} seconds, on the phone during"
      " September 2016.".format(max_number,phone_times[max_number]))
            
            