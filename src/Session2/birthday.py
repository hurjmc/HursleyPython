#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

# Birthday program

# import date functions
from datetime import date

# set up month names
monthName = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("Starting birthday program")

# get today's date
dd = date.today().day
mm = date.today().month
yy = date.today().year


print("Today is - "+str(dd)+"/"+str(mm)+"/"+str(yy)) 
print(" .. or another way - "+str(dd)+" "+monthName[mm-1]+" "+str(yy))

birthday = input("Enter your age (dd/mm/yyyy): ")
birthday = birthday.split(sep="/")

bd_dd = int(birthday[0])
bd_mm = int(birthday[1])
bd_yy = int(birthday[2])

# Check birthday against today's date
if mm > bd_mm:
    print("You have had your birthday already")

elif mm < bd_mm: 
    print("You have to wait for your birthday")

# If we get here their b'day must be this month so check the day
elif dd > bd_dd:   
    print("You had your birthday "+str(dd - bd_dd)+" days ago")

elif dd < bd_dd:   
    print("Your birthday is in "+str(bd_dd - dd)+" days time")

# Month and day are the same, must be their birthday!!
else:
    print("Awesome! It's your birthday today!!!!!") 
