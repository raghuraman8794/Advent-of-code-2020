#!/usr/bin/env python
# coding: utf-8

# In[20]:


nt = open('aoc_1_1_input.txt').readlines()
input_list = []
for line in nt:
    input_list.append(int(line))
    
count=0
final_output=[]


# In[21]:


for i in input_list:
    for j in input_list:
        for k in input_list:
            if (i+j+k)==2020:
                count = count+1
                final_output.append([i,j,k])
        


# In[19]:


print(144*1876)


# In[22]:


final_output


# In[23]:


print(513*512*995)

