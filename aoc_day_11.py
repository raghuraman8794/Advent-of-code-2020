#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
input_file = open('aoc_11_sample_input.txt').readlines()
input_list=[]
layout_after_iterations=[]
no_of_iterations=100
for line in input_file:
    row=[]
    if(line[-1]=='\n'):
        line=line[:-1]
    for character in line:
        if(character=='.'):
            changed_char=1
        if(character=='L'):
            changed_char=2
        if(character=='#'):
            changed_char=3
        row.append(changed_char)
    input_list.append(row)

m = numpy.array(input_list)
dimensions=m.shape

layout_after_iterations.append(input_list)

def calculate_adjacent_occupied_seats(layout,i,j):
    count = 0
    m = numpy.array(layout)
    dimensions=m.shape
    if(i==0 and j==0):                #top left node
        if(layout[i][j+1] == 3):
            count=count+1
        if(layout[i+1][j] == 3):
            count=count+1
        if(layout[i+1][j+1] == 3):
            count=count+1
        return count
    if(i==0 and j==(dimensions[1]-1)):    #top right node
        if(layout[i][-2] == 3):
            count=count+1
        if(layout[i+1][-1] == 3):
            count=count+1
        if(layout[i+1][-2] == 3):
            count=count+1
        return count
    if(i==(dimensions[0]-1) and j==0):    #bottom left node
        if(layout[-2][j] == 3):
            count=count+1
        if(layout[-2][j+1] == 3):
            count=count+1
        if(layout[-1][j+1] == 3):
            count=count+1
        return count
    if(i==(dimensions[0]-1) and (j==dimensions[1]-1)):    #bottom right node
        if(layout[-2][j] == 3):
            count=count+1
        if(layout[-2][-2] == 3):
            count=count+1
        if(layout[i][-2] == 3):
            count=count+1
        return count
    if(i==0 and j!=0 and (j!=dimensions[1]-1)):           #top row without corner nodes
        if(layout[i][j-1] == 3):
            count=count+1
        if(layout[i+1][j-1] == 3):
            count=count+1
        if(layout[i+1][j] == 3):
            count=count+1
        if(layout[i+1][j+1] == 3):
            count=count+1
        if(layout[i][j+1] == 3):
            count=count+1
        return count
    if(i!=0 and i!=(dimensions[0]-1) and j==0):           #left column without corner nodes
        if(layout[i-1][j] == 3):
            count=count+1
        if(layout[i-1][j+1] == 3):
            count=count+1
        if(layout[i][j+1] == 3):
            count=count+1
        if(layout[i+1][j+1] == 3):
            count=count+1
        if(layout[i+1][j] == 3):
            count=count+1
        return count
    if(i==(dimensions[0]-1) and j!=0 and j!=(dimensions[1]-1)):           #bottom row without corner nodes
        if(layout[i][j-1] == 3):
            count=count+1
        if(layout[i-1][j-1] == 3):
            count=count+1
        if(layout[i-1][j] == 3):
            count=count+1
        if(layout[i-1][j+1] == 3):
            count=count+1
        if(layout[i][j+1] == 3):
            count=count+1
        return count
    if(i!=(dimensions[0]-1) and i!=0 and j==(dimensions[1]-1)):           #right column without corner nodes
        if(layout[i-1][j] == 3):
            count=count+1
        if(layout[i-1][j-1] == 3):
            count=count+1
        if(layout[i][j-1] == 3):
            count=count+1
        if(layout[i+1][j-1] == 3):
            count=count+1
        if(layout[i+1][j] == 3):
            count=count+1
        return count
    if(i!=0 and i!=(dimensions[0]-1) and j!=0 and j!=(dimensions[1]-1)):           #Every node inside the layout
        if(layout[i-1][j-1] == 3):
            count=count+1
        if(layout[i-1][j] == 3):
            count=count+1
        if(layout[i-1][j+1] == 3):
            count=count+1
        if(layout[i][j+1] == 3):
            count=count+1
        if(layout[i+1][j+1] == 3):
            count=count+1
        if(layout[i+1][j] == 3):
            count=count+1
        if(layout[i+1][j-1] == 3):
            count=count+1
        if(layout[i][j-1] == 3):
            count=count+1
        return count


# In[ ]:


def calculate_direction_occupied_seats(layout,i_orig,j_orig):
    count = 0
    m = numpy.array(layout)
    dimensions=m.shape
    if(i_orig==0 and j_orig==0):                #top left node
        i=i_orig
        j=j_orig+1
        while(j<dimensions[1]):       #direction 1
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j+1
        i=i_orig+1
        j=j_orig
        while(i<dimensions[0]):       #direction 2
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
        i=i_orig+1
        j=j_orig+1
        while(j<dimensions[1] and i<dimensions[0]):  #direction 3
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
            j=j+1
        return count
    if(i_orig==0 and j_orig==(dimensions[1]-1)):    #top right node
        i=i_orig
        j=j_orig-1
        while(j>=0):                             #direction 1
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j-1
            
        i=i_orig+1
        j=j_orig
        while(i<dimensions[0]):                  #direction 2
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
        
        i=i_orig+1
        j=j_orig-1   
        while(j>=0 and i<dimensions[0]):         #direction 3
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
            j=j-1
        return count
    if(i_orig==(dimensions[0]-1) and j_orig==0):    #bottom left node
        i=i_orig-1
        j=j_orig
        while(i>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
        i=i_orig-1
        j=j_orig+1
        while(i>=0 and j<dimensions[1]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j+1
        i=i_orig
        j=j_orig+1
        while(j<dimensions[1]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j+1
        return count
    if(i_orig==(dimensions[0]-1) and (j_orig==dimensions[1]-1)):    #bottom right node
        i=i_orig-1
        j=j_orig
        while(i>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
        i=i_orig-1
        j=j_orig-1
        while(i>=0 and j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j-1
        i=i_orig
        j=j_orig-1
        while(j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j-1
        return count
    if(i_orig==0 and j_orig!=0 and (j_orig!=dimensions[1]-1)):           #top row without corner nodes
        i=i_orig
        j=j_orig-1
        while(j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j-1
        i=i_orig+1
        j=j_orig-1
        while(j>=0 and i<dimensions[0]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
            j=j-1
        i=i_orig+1
        j=j_orig
        while(i<dimensions[0]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
        i=i_orig+1
        j=j_orig+1
        while(i<dimensions[0] and j<dimensions[1]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
            j=j+1
        i=i_orig
        j=j_orig+1
        while(j<dimensions[1]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j+1
        return count
    if(i_orig!=0 and i_orig!=(dimensions[0]-1) and j_orig==0):           #left column without corner nodes
        i=i_orig-1
        j=j_orig
        while(i>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
        i=i_orig-1
        j=j_orig+1
        while(i>=0 and j<dimensions[1]):      
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j+1
        i=i_orig
        j=j_orig+1
        while(j<dimensions[1]): 
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j+1
        i=i_orig+1
        j=j_orig+1
        while(i<dimensions[0] and j<dimensions[1]): 
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
            j=j+1
        i=i_orig+1
        j=j_orig
        while(i<dimensions[0]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
        return count
    if(i_orig==(dimensions[0]-1) and j_orig!=0 and j_orig!=(dimensions[1]-1)):           #bottom row without corner nodes
        i=i_orig
        j=j_orig-1
        while(j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j-1
        i=i_orig-1
        j=j_orig-1
        while(j>=0 and i>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j-1
        i=i_orig-1
        j=j_orig
        while(i>=0):   
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
        i=i_orig-1
        j=j_orig+1
        while(i>=0 and j<dimensions[1]):  
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j+1
        i=i_orig
        j=j_orig+1
        while(j<dimensions[1]): 
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j+1
        return count
    if(i_orig!=(dimensions[0]-1) and i_orig!=0 and j_orig==(dimensions[1]-1)):           #right column without corner nodes
        i=i_orig-1
        j=j_orig
        while(i>=0): 
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
        i=i_orig-1
        j=j_orig-1
        while(i>=0 and j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j-1
        i=i_orig
        j=j_orig-1
        while(j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j-1
        i=i_orig+1
        j=j_orig-1
        while(j>=0 and i<dimensions[0]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
            j=j-1
        i=i_orig+1
        j=j_orig
        while(i<dimensions[0]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
        return count
    if(i_orig!=0 and i_orig!=(dimensions[0]-1) and j_orig!=0 and j_orig!=(dimensions[1]-1)):           #Every node inside the layout
        i=i_orig-1
        j=j_orig-1
        while(i>=0 and j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j-1
        i=i_orig-1
        j=j_orig
        while(i>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
        i=i_orig-1
        j=j_orig+1
        while(i>=0 and j<dimensions[1]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i-1
            j=j+1
        i=i_orig
        j=j_orig+1
        while(j<dimensions[1]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j+1
        i=i_orig+1
        j=j_orig+1
        while(j<dimensions[1] and i<dimensions[0]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
            j=j+1
        i=i_orig+1
        j=j_orig
        while(i<dimensions[0]):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            i=i+1
        i=i_orig+1
        j=j_orig-1
        while(i<dimensions[0] and j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j-1
            i=i+1
        i=i_orig
        j=j_orig-1
        while(j>=0):
            if(layout[i][j] == 3):
                count=count+1
                break
            if(layout[i][j] == 2):
                break
            j=j-1
        return count


# In[ ]:


for iteration in range(1,no_of_iterations):
    next_iteration=[]
    for i in range(0,dimensions[0]):
        temp=[]
        for j in range(0,dimensions[1]):
            temp.append(0)
        next_iteration.append(temp)
    layout_after_iterations.append(next_iteration)
        
    for i in range(0,dimensions[0]):
        for j in range(0,dimensions[1]):
            #if(layout_after_iterations[iteration-1][i][j]==2 and ((calculate_adjacent_occupied_seats(layout_after_iterations[iteration-1],i,j))==0 or (calculate_direction_occupied_seats(layout_after_iterations[iteration-1],i,j))==0)):
            if(layout_after_iterations[iteration-1][i][j]==2 and  (calculate_direction_occupied_seats(layout_after_iterations[iteration-1],i,j))==0):
                layout_after_iterations[iteration][i][j]=3
            elif(layout_after_iterations[iteration-1][i][j]==3 and (calculate_direction_occupied_seats(layout_after_iterations[iteration-1],i,j))>=5):
                layout_after_iterations[iteration][i][j]=2
            elif(layout_after_iterations[iteration-1][i][j]==1 ):
                layout_after_iterations[iteration][i][j]=1
            else:
                layout_after_iterations[iteration][i][j]=layout_after_iterations[iteration-1][i][j]
                
    diff_between_iteration=[]
    for i in range(0,dimensions[0]):
        temp=[]
        for j in range(0,dimensions[1]):
            temp.append(0)
        diff_between_iteration.append(temp)
        
    for i in range(0,dimensions[0]):
        for j in range(0,dimensions[1]):
            diff_between_iteration[i][j]=layout_after_iterations[iteration][i][j] - layout_after_iterations[iteration-1][i][j]
    
    count=0
    for i in range(0,dimensions[0]):
        for j in range(0,dimensions[1]):
            count=count+diff_between_iteration[i][j]
    
    if(count==0):
        print("chaos has stabilized")
        break


# In[ ]:


#layout_after_iterations


# In[ ]:


final=layout_after_iterations[-1]
final_ans=0
for i in range(0,dimensions[0]):
    for j in range(0,dimensions[1]):
        if(final[i][j]==3):
            final_ans=final_ans+1
            
print("final_ans = ",final_ans)

