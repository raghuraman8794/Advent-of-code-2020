#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import combinations 

input_file = open('aoc_10_sample_input.txt').readlines()
input_list=[0]
for line in input_file:
    input_list.append(int(line))
    
input_list2=input_list.sort()

diff=[]
for i in range(1,len(input_list)):
    temp=input_list[i]-input_list[i-1]
    diff.append(temp)
no_of_diff_1=0
no_of_diff_3=0
for i in diff:
    if(i==1):
        no_of_diff_1=no_of_diff_1+1
    elif(i==3):
        no_of_diff_3=no_of_diff_3+1
no_of_diff_3=no_of_diff_3+1

final_ans_first_part=no_of_diff_1*no_of_diff_3
#print(final_ans_first_part)

input_list.append(input_list[-1]+3)

delimited_input_list=[]
upper_limit=0
for i in range(0,len(input_list)-1):
    if((input_list[i+1]-input_list[i])==3):
        delimited_input_list.append(input_list[upper_limit:(i+1)])
        upper_limit=(i+1)

#delimited_input_list[-1]=delimited_input_list[-1][:-1]
#delimited_input_list[-1].append((delimited_input_list[-1][-1])+3)


# In[ ]:


permu_count=[]
for i in delimited_input_list:
    a=i[1:-1]
    count=0
    for j in range(0,len(a)+1):
        comb=combinations(a,j)
        for k in list(comb):
            count=count+1
    if(i[-1]-i[0]==4):
        count=count-1
    permu_count.append(count)
    
prod=1
for i in permu_count:
    prod=prod*i
    
final_ans_sec_part=prod
print(final_ans_sec_part)

