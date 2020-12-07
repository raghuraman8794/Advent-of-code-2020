#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_file = open('aoc_7_sample_input.txt').readlines()

our_bag='shiny gold'
count=0
layer=[]
for i in range(0,100):
    layer.append([])
    
first_layer=[]
layer_count=0

for line in input_file:
    count=count+1
    if our_bag in line:
        index=line.find(our_bag)
        if(index==0):
            continue
        temp1=line.split(' ')
        temp2=temp1[0]
        temp3=temp1[1]
        temp4=temp2+" "+temp3
        layer[layer_count].append(temp4)                 

        
layer_count=layer_count+1           


# In[2]:


def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
            
    return unique_list


# In[3]:


no_of_iterations=99
for i in range(0,no_of_iterations):
    for colour in layer[layer_count-1]:
        for line in input_file:
            if colour in line:
                index=line.find(colour)
                if(index==0):
                    continue
                temp1=line.split(' ')
                temp2=temp1[0]
                temp3=temp1[1]
                temp4=temp2+" "+temp3
                layer[layer_count].append(temp4)
    
    layer[layer_count]=unique(layer[layer_count])       
    layer_count=layer_count+1


# In[4]:


total=0
for i in range(0,100):
    total=total+len(layer[i])


# In[5]:


layer


# In[6]:


total

