#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_file = open('aoc_9_sample_input.txt').readlines()
input_list=[]
for line in input_file:
    input_list.append(int(line))


# In[2]:


preamble_length=25
upper_limit=0
lower_limit=preamble_length
index_of_black_sheep=0
for i in range(preamble_length,len(input_list)):
    target_sum_flag=0
    target_sum=input_list[i]
    for j in range(upper_limit,lower_limit):
        for k in range(upper_limit,lower_limit):
            if(input_list[j]==input_list[k]):
                continue
            if((input_list[j]+input_list[k])==target_sum):
                target_sum_flag=1
    if(target_sum_flag==0):
        print("The black sheep number is : ",target_sum)
        index_of_black_sheep=i
        break
    upper_limit=upper_limit+1
    lower_limit=lower_limit+1


# In[3]:


for i in range(0,(index_of_black_sheep+1)):
    final_list=[]
    for j in range(i,(index_of_black_sheep+1)):
        #print("i",i)
        #print('final_list',final_list)
        final_list.append(input_list[j])
        if(sum(final_list)==target_sum):
            print(final_list)
            break
        


# In[9]:


final_list=[3204444, 2173398, 2458349, 2954632, 3840898, 2963655, 2955986, 3558383, 2709364, 5235843, 3276412, 2745070, 2798952, 3214700, 5160364, 3946784, 3997835]


# In[10]:


smallest_num=min(final_list)
largest_num=max(final_list)

final_sum=smallest_num+largest_num
print(final_sum)

