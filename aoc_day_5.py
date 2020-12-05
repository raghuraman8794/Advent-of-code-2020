#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def find_seat_id(string):
    string_input=string
    lower_limit=0
    upper_limit=127
    left_limit=0
    right_limit=7
    for letter in string_input:
        if (letter=='F'):
            lower_limit=lower_limit
            upper_limit=math.floor((upper_limit-lower_limit)/2) + (lower_limit)
        if (letter=='B'):
            upper_limit=upper_limit
            lower_limit=math.ceil((upper_limit-lower_limit)/2) + (lower_limit)
        if (letter=='L'):
            left_limit=left_limit
            right_limit=math.floor((right_limit-left_limit)/2) + (left_limit)
        if (letter=='R'):
            right_limit=right_limit
            left_limit=math.ceil((right_limit-left_limit)/2) + (left_limit)
            
    seat_id=(upper_limit*8)+right_limit
    return seat_id


# In[ ]:


input_file = open('aoc_5_1_input.txt').readlines()
all_seat_ids=[]
for line in input_file:
    all_seat_ids.append(find_seat_id(line))


# In[ ]:


for seat in all_seat_ids:
    seat=int(seat)


# In[ ]:


for i in range(0,964):
    if i not in all_seat_ids:
        print(i)

