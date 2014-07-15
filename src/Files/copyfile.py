'''
Created on 21 Oct 2013

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
# Copy selected lines from SOURCE_FILE to TARGET_FILE
#

# 'Constants'
SOURCE_FILE_NAME = 'sourcefile.txt'
TARGET_FILE_NAME = 'wordfile.txt'
SUB_DIR_NAME = 'data1'

# Tell the user where we are
print(os.path.abspath('.'))

# First create a sub-directory if required
if (os.path.exists(SUB_DIR_NAME)):
    print("found directory", SUB_DIR_NAME)
else: 
    print("creating data directory", SUB_DIR_NAME)     
    os.mkdir(SUB_DIR_NAME)

target = os.path.join(SUB_DIR_NAME, TARGET_FILE_NAME)

# Ask where the source file is
source_directory = input('Enter source directory')

# Create full source file name
source = os.path.join(source_directory, SOURCE_FILE_NAME)

# Make sure source exists
if os.path.isfile(source):
    source_file = open(source,"r")
    target_file = open(target,"w")
    
    # For each line in the file which does not start with 'x'
    # copy it to a new file 
    for line in source_file:
        if line[0] != 'x':
            target_file.write(line)
    
    # Tidy up by closing the source and target files
    source_file.close()
    target_file.close()
             
# Tell the user if it is not there 
else:
    print ("File",source,"not found") 
    
    