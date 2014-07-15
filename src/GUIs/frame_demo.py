#========================================================# 
#  (C) COPYRIGHT IBM CORP. 2014 ALL RIGHTS RESERVED      #  
#                                                        # 
#  Provided for use as educational material.             #
#                                                        # 
#  Redistribution for other purposes is not permitted.   #  
#========================================================#

#
# tkinter - frame demo
#
import tkinter as tk

def b_cmd(x):
    print("Pressed",x) 

root = tk.Tk()

label = tk.Label(root,text='LABEL')
label.pack(side=tk.LEFT)

number_pad = tk.Frame(root,bg='red')
number_pad.pack(side=tk.RIGHT)

for i in range(9):
    print(i//3,i%3)
    button = tk.Button(number_pad,text=str(i+1))
    button.grid(row=i//3,column=i%3,sticky=tk.E+tk.W)
    button['command'] = (lambda b = (i+1): b_cmd(b))

button = tk.Button(number_pad,text='0')
button.grid(row=3,column=0,columnspan=3,sticky=tk.E+tk.W)
button['command'] = (lambda b = 0: b_cmd(b))

root.mainloop()

