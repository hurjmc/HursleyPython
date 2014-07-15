#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

# try using 'for' statement
print("Starting 'for' test")

reply = input("enter a number less than 20: ")
maxvalue = int(reply)

for i in range(maxvalue):
    print(i) 
