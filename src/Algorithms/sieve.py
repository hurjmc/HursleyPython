'''
Created on 19 Oct 2013

@author: whittin

'''
#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

# Generate primes using sieve method:

# INPUT maxprime
reply = input("Enter maximum prime:")
maxprime = int(reply)

# Create integer array called primes with maxprime values
# Initialise primes so that for all x  prime[x] = x  
primes = list(range(maxprime))

# Show 1 is not prime by setting primes[1] = 0
primes[1] = 0

# Initialise current_prime  = 2
current_prime = 2

# WHILE current_prime is less than length of primes 
while current_prime < maxprime:

    # IF  primes[current_prime] indicates a prime (it is not 0) THEN
    if primes[current_prime] != 0:
                
        # Initialise counter to square of current_prime
        counter = current_prime**2
        
        #  WHILE counter less than length of primes 
        #     mark primes[counter] as not prime by setting to 0
        while counter < maxprime:
            primes[counter] =  0
            counter += current_prime 

    current_prime += 1 
                 
#
# FOR k = 0 TO size of primes
#    IF primes[k] is not  0 THEN
#        k must be a prime so print it 
#    END IF
# NEXT k
#
for p in primes:
    if p != 0 :
        print (str(p).rjust(4),end=" ")
        
