#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

# Shapes module 

# Calculate circle area
def circleArea(radius=1):
    from math import pi
    area = pi*radius*radius
    return area

def rectangleInfo(width,height):
    area = width*height
    perimeter = 2*(width+height)
    print("For rectangle (", width,"x",height,")",
          "area =",area,
          "and perimeter =",perimeter)
