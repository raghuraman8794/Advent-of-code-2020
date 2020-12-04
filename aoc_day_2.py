#!/usr/bin/env python
# coding: utf-8

# In[42]:


input_file = open('aoc_2_1_input.txt').readlines()
input_list = []
for line in input_file:
    input_list.append(line)


# In[6]:


sample_input='8-9 n: nnnnnnnnn'
value = sample_input.split(' ')
limits=value[0].split('-')
low_limit=limits[0]
high_limit=limits[1]

letter=value[1][0]

string=value[2]

final_count=string.count(letter)


# In[47]:


final_pass=0
for line1 in input_list:
    value = line1.split(' ')
    limits=value[0].split('-')
    first_pos=limits[0]
    sec_pos=limits[1]
    letter=value[1][0]
    string=value[2]
    print(first_pos)
    print(sec_pos)
    print('letter=',letter)
    for i in range(0,len(string)):

        if(string[i]==letter and ((i+1)==int(first_pos) or (i+1)==int(sec_pos))):
            if(string[int(first_pos)-1]==string[int(sec_pos)-1]):
                break
            final_pass=final_pass+1
            print("string",line1)
            break


# In[48]:


final_pass


# In[23]:


for i in range(0,5):
    print(i)

