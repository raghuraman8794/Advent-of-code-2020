#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re 


# In[2]:


input_file = open('aoc_4_1_input_sample.txt').readlines()
line_number=0
passport_number=1
input_list = []
for line in input_file:
    if(line[0]!='\n'):
        line=line[:-1]
        line=line + (" ")
    input_list.append(line)
    line_number=line_number+1
    


# In[3]:


valid_passport=0
byr_present=0
iyr_present=0
eyr_present=0
hgt_present=0
hcl_present=0
ecl_present=0
pid_present=0
temp_count=0
line_counter=0
new_input_list=[]

for line in input_list:
    line_counter=line_counter+1
    if(line[0]!='\n'):
        temp_count=temp_count+1
        if "byr" in line :
            byr_present=1
        if "iyr" in line :
            iyr_present=1
        if "eyr" in line :
            eyr_present=1
        if "hgt" in line :
            hgt_present=1
        if "hcl" in line :
            hcl_present=1
        if "ecl" in line :
            ecl_present=1
        if "pid" in line :
            pid_present=1
    if(line[0]=='\n'):
        temp_count=0
        byr_present=0
        iyr_present=0
        eyr_present=0
        hgt_present=0
        hcl_present=0
        ecl_present=0
        pid_present=0
    if (byr_present==1 and iyr_present==1 and eyr_present==1 and hgt_present==1 and hcl_present==1 and ecl_present==1 and pid_present==1):
        valid_passport=valid_passport+1
        for i in range(0,temp_count):
            new_input_list.append([input_list[line_counter-i-1]])
        new_input_list.append('\n')
        


# In[4]:


temp_count=0
line_counter=0
pre_final_input_list=[]
for i in range(0,valid_passport):
    pre_final_input_list.append([])
counter_for_new_list=0
for line in new_input_list:
    
    line_counter=line_counter+1
    
    if(line=='\n'):
        for i in range(0,temp_count):
            pre_final_input_list[counter_for_new_list]=pre_final_input_list[counter_for_new_list]+new_input_list[line_counter-i-2]
        counter_for_new_list=counter_for_new_list+1
        temp_count=0
    if(line!='\n'):
        temp_count=temp_count+1



# In[5]:


pre_final_input_list


# In[6]:


final_list=[]
line_counter=0
counter_for_new_list=0
for i in range(0,valid_passport):
    final_list.append([])

for line in pre_final_input_list:
    final_list[counter_for_new_list]=pre_final_input_list[line_counter][0]
    for i in range(1,len(pre_final_input_list[line_counter])):
        final_list[counter_for_new_list]=final_list[counter_for_new_list]+pre_final_input_list[line_counter][i]
        
    line_counter=line_counter+1
    counter_for_new_list=counter_for_new_list+1
    


# In[7]:


final_list


# In[8]:


valid_passport=0;

for line in final_list:
    byr_valid=0
    iyr_valid=0
    eyr_valid=0
    hgt_valid=0
    hcl_valid=0
    ecl_valid=0
    pid_valid=0
    space_split=line.split(" ")
    for item in space_split:
        entities=item.split(":")
        if(entities[0]=='byr'):
            if(int(entities[1])>=1920 and int(entities[1])<=2002):
                byr_valid=1
        if(entities[0]=='iyr'):
            if(int(entities[1])>=2010 and int(entities[1])<=2020):
                iyr_valid=1
        if(entities[0]=='eyr'):
            if(int(entities[1])>=2020 and int(entities[1])<=2030):
                eyr_valid=1
        if(entities[0]=='hcl'):
            if(entities[1][0]=='#'):
                entities[1]=entities[1:]
                res_num = ''.join(filter(lambda i: i.isdigit(), entities[1])) 
                res_alpha=''.join(filter(lambda i: i.isalpha(), entities[1]))
                num_true=0
                alpha_true=0
                for i in res_num:
                    if(i>='0' and i<='9'):
                        num_true=num_true+1
                for i in res_alpha:
                    if(i>='a' and i<='f'):
                        alpha_true=alpha_true+1
                if(num_true==len(res_num) and alpha_true==len(res_alpha)):
                    hcl_valid=1
        if(entities[0]=='hgt'):
                res_num = ''.join(filter(lambda i: i.isdigit(), entities[1])) 
                res_alpha=''.join(filter(lambda i: i.isalpha(), entities[1]))
                if(res_alpha=='cm'):
                    if(int(res_num)>=150 and int(res_num)<=193):
                        hgt_valid=1
                if(res_alpha=='in'):
                    if(int(res_num)>=59 and int(res_num)<=76):
                        hgt_valid=1
            
        if(entities[0]=='ecl'): 
            if(entities[1]=='amb' or entities[1]=='blu' or entities[1]=='brn' or entities[1]=='gry' or entities[1]=='grn' or entities[1]=='hzl' or entities[1]=='oth'):
                ecl_valid=1
        if(entities[0]=='pid'):
            if(len(entities[1])==9):
                pid_valid=1
                
    if (byr_valid==1 and iyr_valid==1 and eyr_valid==1 and hgt_valid==1 and hcl_valid==1 and ecl_valid==1 and pid_valid==1):
            valid_passport=valid_passport+1
                
        
            
            


# In[9]:


valid_passport

