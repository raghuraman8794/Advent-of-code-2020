#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input_file = open('aoc_8_sample_input.txt').readlines()
input_list=[]
for line in input_file:
    list=line.split(" ")
    if(list[-1][-1]=='\n'):
        list[-1]=list[-1][:-1]
        input_list.append(list)
    else:
        input_list.append(list)
        


# In[ ]:


def calculate_acc(input_list):
    line_flag_array=[]
    for i in range(0,len(input_list)):
        line_flag_array.append(0)
    
    count_nop=0
    index_of_nop=[]
    count_jmp=0
    index_of_jmp=[]

    acc=0
    break_flag=0
    i=0
    while(break_flag==0):
    
        line_flag_array[i]=line_flag_array[i]+1
        if(line_flag_array[i]>1):
            break_flag=break_flag+1
            instruction=input_list[i][0]
            continue
    
        instruction=input_list[i][0]

        sign=input_list[i][1][0]

        number=input_list[i][1][1:]
    
        if(instruction=='acc'):
            if(sign=='+'):
                acc=acc+int(number)
            if(sign=='-'):
                acc=acc-int(number)
            i=i+1
        elif(instruction=='jmp'):
            count_jmp=count_jmp+1
            index_of_jmp.append(i)
            if(sign=='+'):
                i=i+int(number)
            elif(sign=='-'):
                i=i-int(number)
        if(instruction=='nop'):
            index_of_nop.append(i)
            count_nop=count_nop+1
            i=i+1
        
        if(i>len(input_list)):
            i=i%(len(input_list))
        elif (i<0):
            i=i*(-1)
            i=i%(len(input_list))
            i=i*(-1)
            i=(len(input_list))+i
        print(acc)
    return [acc,index_of_nop,index_of_jmp]


# In[ ]:


result=calculate_acc(input_list)
index_of_nop=result[1]
index_of_jmp=result[2]


# In[ ]:


modified_input_list1=[] #nop to jmp converted list
modified_input_list2=[] #jmp to nop converted list

for i in index_of_nop:
    input_list=[]
    for line in input_file:
        list=line.split(" ")
        if(list[-1][-1]=='\n'):
            list[-1]=list[-1][:-1]
            input_list.append(list)
        else:
            input_list.append(list)
    modified_input_list1.append(input_list)
    modified_input_list1[-1][i][0]='jmp'

        
for i in index_of_jmp:
    input_list=[]
    for line in input_file:
        list=line.split(" ")
        if(list[-1][-1]=='\n'):
            list[-1]=list[-1][:-1]
            input_list.append(list)
        else:
            input_list.append(list)
    modified_input_list2.append(input_list)
    modified_input_list2[-1][i][0]='nop'
        


# In[ ]:


acc_1=[]
for input_list in modified_input_list1:
    acc=calculate_acc(input_list)
    acc_1.append(acc[0])


# In[ ]:


acc_2=[]
for input_list in modified_input_list2:
    acc=calculate_acc(input_list)
    acc_2.append(acc[0])

