#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#
#
# Calculate average of entered values:
#

import sys

print (sys.path)

try:
    count = 0
    total = 0 

    #REPEAT 
    while True:
        # INPUT  x
        x = int(input("Enter integer:"))
        count += 1
        total += x   

        # INPUT  more
        more = input("Any more? [Y or N]")
        more = more.upper()

        # UNTIL  more  is not 'yes'
        if more[0] != 'Y':
            break  
except Exception as inst:
    print("Unexpected error:", inst)

#Calculate average
print ("Average is ",total/count)
input('press enter to exit')
