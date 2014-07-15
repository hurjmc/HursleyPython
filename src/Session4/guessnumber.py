#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#


def mid_point(minimum, maximum):
    '''This is a function that takes two integers as its input
    and returns the middle value between them (also as an integer).
    '''
    extent = maximum - minimum
    mid_extent = extent // 2
    middle = minimum + mid_extent
    return middle


def testMidPoint(minimum, maximum):
    '''This is a simple function that takes two numbers, finds their mid-point
    and prints out the three numbers so you can check that they are correct 
    '''
    middle = mid_point(minimum, maximum)
    print("The mid point of " + str(minimum) + 
          " and " + str(maximum) + " is " + str(middle)) 


print ("Think of a number between 1 and 100")
minimum = 0
maximum = 101
found = False

while found == False:
    guessValue = mid_point(minimum, maximum)
    print ("range is now between " + str(minimum) + " and " + str(maximum))
    reply = input("Is your number " + str(guessValue) + " ? yes, higher or lower (y, h, l)")

    if reply == "h" :
        minimum = guessValue
    elif (reply == "l") :
        maximum = guessValue
    else:
        print("I guessed correctly. Its " + str(guessValue))
        found = True


