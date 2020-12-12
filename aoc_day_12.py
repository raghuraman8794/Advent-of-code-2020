#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#First part

direction_facing=['E','S','W','N']
input_file = open('aoc_12_sample_input.txt').readlines()
input_list=[]
for line in input_file:
    input_list.append((line))
    
direction='E'
direction_moving='E'

final_values = {
  "E": 0,
  "S": 0,
  "W": 0,
  "N": 0
}

x=0
y=0
for i in range(0,len(input_list)):
    action=input_list[i][0]
    value=int(input_list[i][1:4])
    if(action=='F' and (direction=='E' or direction=='S' or direction=='W' or direction=='N')):
        if(direction=='E'):
            x=x+value
        if(direction=='N'):
            y=y+value
        if(direction=='W'):
            x=x-value
        if(direction=='S'):
            y=y-value
    if(action=='R'):
        value=value/90
        value=value+direction_facing.index(direction)
        direction=direction_facing[(int(value)%4)]
    if(action=='L'):
        value=value/90
        value=direction_facing.index(direction) - value
        direction=direction_facing[int(value)]
    if(action=='E' or action=='S' or action=='W' or action=='N'):
        if(action=='E'):
            x=x+value
        if(action=='N'):
            y=y+value
        if(action=='W'):
            x=x-value
        if(action=='S'):
            y=y-value
        
    print('x:',x,' y:',y)
        
    


# In[ ]:


#Second part

import math 

input_file = open('aoc_12_sample_input.txt').readlines()
input_list=[]
for line in input_file:
    input_list.append((line))

x=0
y=0
waypoint_x=x+10
waypoint_y=y+1

for i in range(0,len(input_list)):
    action=input_list[i][0]
    value=int(input_list[i][1:4])
    if(action=='F'):
        x=x+(value*waypoint_x)
        y=y+(value*waypoint_y)
    if(action=='R'):
        value=math.radians(value)
        xa=waypoint_x
        ya=waypoint_y
        waypoint_x = x + ((xa) * math.cos(value)) + ((ya) * math.sin(value))
        waypoint_y = y - ((xa) * math.sin(value)) + ((ya) * math.cos(value))
        waypoint_x=int(waypoint_x-x)
        waypoint_y=int(waypoint_y-y)
    if(action=='L'):
        value=math.radians(value)
        value=-1*value
        xa=waypoint_x
        ya=waypoint_y
        waypoint_x = x + ((xa) * math.cos(value)) + ((ya) * math.sin(value))
        waypoint_y = y - ((xa) * math.sin(value)) + ((ya) * math.cos(value))
        waypoint_x=int(waypoint_x-x)
        waypoint_y=int(waypoint_y-y)

    if(action=='E' or action=='S' or action=='W' or action=='N'):
        if(action=='E'):
            waypoint_x=waypoint_x+value
        if(action=='N'):
            waypoint_y=waypoint_y+value
        if(action=='W'):
            waypoint_x=waypoint_x-value
        if(action=='S'):
            waypoint_y=waypoint_y-value
        
    print('i:',i+1)
    print('action:',action)
    print('value:',value)
    print('x:',x,' y:',y)
    print('waypoint_x:',waypoint_x,' waypoint_y:',waypoint_y)
        
    

