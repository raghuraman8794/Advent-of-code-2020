#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_file = open('aoc_6_input_sample.txt').readlines()
letter_flags=[]
for i in range(0,26):
    letter_flags.append(0)
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count_of_each_group=[]


# In[2]:


group=1
group_length=0
group_length_list=[]
for line in input_file:
    if(line[0]=='\n'):
        group=group+1
        group_length_list.append(group_length)
        group_length=0
    else:
        group_length=group_length+1


# In[3]:


group=1
group_length=0
group_id=0
final_sum=[]
for line in input_file:
    if(line[0]=='\n'):
        count_of_each_group.append(sum(letter_flags))
        for i in letter_flags:
            if (i==group_length_list[group_id]):
                final_sum.append(1)
        for i in range(0,26):
            letter_flags[i]=0
        group_id=group_id+1
    else:
        for character in line:
            if character in letters:
                if((letter_flags[letters.index(character)])==group_length_list[group_id]):
                    letter_flags[letters.index(character)] = 1
                else:
                    letter_flags[letters.index(character)] = letter_flags[letters.index(character)]+1   


# In[4]:


sum(final_sum)

