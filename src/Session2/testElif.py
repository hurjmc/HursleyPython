#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

# 'elif'  test

# Get score from console
reply = input("Enter your score: ")
score = int(reply)

# Check score and print comment
if score <= 10:
    print("Pathetic!!!")

elif score <= 50: 
    print("Granny could do better!!")

elif score <= 60: 
    print("Getting there!")

elif score <= 70: 
    print("Cool!!")

elif score <= 100: 
    print("Awesome!!!")    

else:
    print("You must have cheated, the test is out of 100!!!") 

