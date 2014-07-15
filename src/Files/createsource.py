'''
Created on 22 Oct 2013

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
from random import shuffle,choice

#
# Copy selected lines from SOURCE_FILE to TARGET_FILE
#

# 'Constants'
INPUT_FILE_NAME = 'rawsource.txt'
OUTPUT_FILE_NAME = 'sourcefile.txt'
SUB_DIR_NAME = 'c:\\Temp'

# Tell the user where we are
print(os.path.abspath('.'))

source_file = os.path.join(SUB_DIR_NAME, INPUT_FILE_NAME)
target_file = os.path.join(SUB_DIR_NAME, OUTPUT_FILE_NAME)

try:
    source_file = open(source_file,"r")
    target_file = open(target_file,"w")
 
except FileNotFoundError as fnf:
    print("could not find the file",fnf.filename)    

words = []    
for line in source_file:
    words.append(line.strip())

source_file.close() 

print("Found",len(words),"words") 


shuffle(words)

while len(words) > 0:
    indent = choice(range(5))
    oline = 'x'*indent
    w  = choice(range(6,9))
    for a in range(w):
        xword = words.pop()
        oline = oline + ',' + xword
    
    target_file.write(oline+"\n")

