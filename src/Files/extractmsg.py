'''
Created on 1 Nov 2013

@author: whittin
'''

#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#


import os.path

#
# Extract words from 'data/wordfile.txt' which do not have 5 letters
#

# 'Constants'
SOURCE_FILE_NAME = 'wordfile.txt'
SUB_DIR_NAME = 'data'

# Set up source file name and open it
source = os.path.join(SUB_DIR_NAME, SOURCE_FILE_NAME)
source_file =  open(source,"r") 

# For each line in the file
# - extract all the words on the line
# - print each word NOT 5 characters long 
for line in source_file:
    
    # remove the 'new-line' character
    line_no_nl = line.strip() 
    
    # split line at each ',' 
    words = line_no_nl.split(sep=',')
    
    # Print word if its length is not 5 
    for word in words:
        if len(word) != 5:  
            print (word)

# Close the file    
source_file.close()     