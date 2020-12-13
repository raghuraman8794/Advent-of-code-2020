#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#First Part

input_file = open('aoc_13_sample_input.txt').readlines()
input_list=[]
for line in input_file:
    input_list.append((line))

my_timestep=int(input_list[0])   
bus_ids_temp=input_list[1].split(',')
bus_ids=[]
for i in bus_ids_temp:
    if(i!='x'):
        bus_ids.append(int(i))

final_time_steps=[]
for i in bus_ids:
    temp1=i
    temp2=[0]
    while(temp2[-1]<my_timestep):
        temp2.append(temp2[-1] + temp1)
    temp3=[temp1,temp2]
    final_time_steps.append(temp3)

final_diff=[]
for i in final_time_steps:
    bus_id=i[0]
    diff=(i[1][-1]) - my_timestep
    #temp=[diff]
    final_diff.append(diff)
    
minimum_time_bus_id=min(final_diff)

for i in range(0,len(final_diff)):
    if (final_diff[i]==minimum_time_bus_id):
        final_bus_id=bus_ids[i]

final_ans=minimum_time_bus_id*final_bus_id
print(final_ans)


# In[ ]:


bus_ids


# In[ ]:


#Second Part

input_file = open('aoc_13_sample_input.txt').readlines()
input_list=[]
for line in input_file:
    input_list.append((line))
    
bus_ids_temp=input_list[1].split(',')
bus_ids=[]
for i in bus_ids_temp:
        bus_ids.append((i))


# In[ ]:


break_loop=0    
t=1
while (break_loop==0):
    if((t%13)==0):
        if((t+3)%41==0):
            if((t+13)%569==0):
                if((t+15)%29==0):
                    if((t+32)%19==0):
                        if((t+36)%23==0):
                            if((t+44)%937==0):
                                if((t+50)%37==0):
                                    if((t+61)%17==0):
                                        break_loop=1
    t=t+1
    
final_ans=t-1
print(final_ans)


# In[ ]:


break_loop=0    
t=1
while (break_loop==0):
    if((t%7)==0):
        if((t+1)%13==0):
            if((t+4)%59==0):
                if((t+6)%31==0):
                    if((t+7)%19==0):
                        break_loop=1
    t=t+1
    
final_ans=t-1
print(final_ans)


# In[ ]:


import numpy as np
divisor_list = [7,13]
print(int(np.lcm.reduce(divisor_list)))


# In[ ]:


from sympy.ntheory.modular import crt


# In[ ]:


a=crt([7,13,59,31,19],[0,12,55,25,12])


# In[ ]:


a=crt([13,41,569,29,19,23,937,37,17],[0,(41-3),(569-13),(29-15),(19-32),(23-36),(937-44),(37-50),(17-61)])

