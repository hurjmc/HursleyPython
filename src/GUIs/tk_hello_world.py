#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

#
# TKinter 'Hello World! program
#

import tkinter as tk

def button_command():
    print ("Button pressed!")

root = tk.Tk()

message = tk.Label(root,text="Hello World!")
message.pack()

button = tk.Button(root,text='BUTTON')
button['command'] = button_command
button.pack()

root.mainloop()
