#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

# times table program
reply = input("Enter a number between 1 and 30: ")
size = int(reply)
print ("Showing the (" + reply + "x" + reply + ") times table")

size = size + 1
for row in range (1,size):
    for column in range(1,size):
        multiple = row*column
        print(repr(multiple).rjust(4) , end="  ")
    
    print("")
