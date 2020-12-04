#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy
import math


# In[2]:


input_file = open('aoc_3_1_input.txt').readlines()
no_of_rows=0
i=0
input_list1 = []
for line in input_file:
    no_of_col=0
    single_line=[]
    for character in line:
        no_of_col=no_of_col+1
        single_line.append(character)
    if(i!=322):
        single_line.pop()
    input_list1.append(single_line)
    print(len(input_list1[i]))
    no_of_rows=no_of_rows+1
    i=i+1

no_of_repeat=(math.ceil((no_of_rows*3)/no_of_col))*5


# In[ ]:


type(i)


# In[3]:


i=0
for line in input_list1:
    input_list1[i]=input_list1[i]*no_of_repeat
    print(len(input_list1[i]))
    i=i+1


# In[4]:


i=0
j=0
max_rows=no_of_rows
max_cols=len(input_list1[0])
no_of_trees1=0
no_of_trees2=0
no_of_trees3=0
no_of_trees4=0
no_of_trees5=0


while(i<max_rows):
        i=i+1
        j=j+3
        if(i>=max_rows or j>=max_cols):
            break
        if(input_list1[i][j]=='1'):
            no_of_trees1=no_of_trees1+1
print("no_of_trees1",no_of_trees1)
print(i)
print(j)
            
i=0
j=0
            
while(i<max_rows):
        i=i+1
        j=j+1
        if(i>=max_rows or j>=max_cols):
            break
        if(input_list1[i][j]=='1'):
            no_of_trees2=no_of_trees2+1
print("no_of_trees2",no_of_trees2)
print(i)
print(j)
            
i=0
j=0
            
while(i<max_rows):
        i=i+1
        j=j+5
        if(i>=max_rows or j>=max_cols):
            break
        if(input_list1[i][j]=='1'):
            no_of_trees3=no_of_trees3+1
            
print("no_of_trees3",no_of_trees3)           
print(i)
print(j)
            
i=0
j=0
            
while(i<max_rows):
        i=i+1
        j=j+7
        if(i>=max_rows or j>=max_cols):
            break
        if(input_list1[i][j]=='1'):
            no_of_trees4=no_of_trees4+1
            
print("no_of_trees4",no_of_trees4)
print(i)
print(j)
            
i=0
j=0
            
while(i<max_rows):
        i=i+2
        j=j+1
        if(i>=max_rows or j>=max_cols):
            break
        if(input_list1[i][j]=='1'):
            no_of_trees5=no_of_trees5+1
            
print("no_of_trees5",no_of_trees5)
print(i)
print(j)


# In[5]:


total_no_of_trees=no_of_trees1*no_of_trees2*no_of_trees3*no_of_trees4*no_of_trees5
total_no_of_trees


# In[ ]:


max_rows


# In[ ]:


len(input_list1[-1])

