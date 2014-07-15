'''
Created on 15 Nov 2013

@author: whittin
'''

#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#


def find_city(file, city):
    for line in file:
        if line.startswith(city):
            break
        
    return line


if __name__ == '__main__':
    filename = input("Enter file name: ")
    city = input("Enter city name: ")
    file = open(filename,"r")
    temps = find_city(file, city)
    
    if temps.startswith(city):
        print(temps)
    else:
        print("Data for",city,"not found.")
        
        