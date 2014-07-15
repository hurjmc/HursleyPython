'''
Created on 20 Oct 2013

@author: whittin
'''
#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

direction = "WEST"
def move(d):
    pass

direction = "WEST"
def bad_move(d):
    pass
A,B = 1,2
# Set MAX equal to the largest  value  in 
# variables A and B:
if A > B:
    MAX = A
else:
    MAX = B
      

# Process direction variable:
# SELECT CASE direction OF
#    north:  move up
if direction == 'NORTH':
    move("UP") 

#    south:  move down
elif direction == 'SOUTH':
    move("DOWN") 
    
#    east: move right 
elif direction == 'EAST':
    move("RIGHT") 
    
#    west: move left
elif direction == 'WEST':
    move("LEFT") 

#    OTHERWISE  error
else:
    bad_move(direction) 
    
#Print Fibonacci numbers less than MAX :

A = 0
B = 1

#WHILE  B less than MAX
while B < MAX :
    print (B)
    temp =A+B
    A = B
    B  = temp
    
    
def process_item(e):
    pass        

A = [1,2,3,4]
# Process each element in an Array ‘A’:

#FOR  k = 1 TO size of A
#           process A(k)= A
for k in range(len(A)):
    process_item(A[k])
       
    
    

