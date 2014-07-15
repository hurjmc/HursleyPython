#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#


# Try out if statement 
print("Starting 'if' test!")

reply = input("Enter a number more than 5 and not more than 10: ")    
i = int(reply)

if i > 5:
    if i <= 10:
        print("OK!")
    else:
        print("Number too high!")     
else:
    print("Number too low!")


